import logging.config
import os
import traceback

from celery import Celery
from celery.schedules import crontab

import server.tasks.v1
from resources.sites import sites_list

from server.config import DatabaseConfig, CeleryConfig, get_celery_config, get_database_config
from server.database import registry_database

celery_config: CeleryConfig = get_celery_config()

if not os.path.exists('logs'):
    os.mkdir('logs')

logging.config.fileConfig(celery_config.logging_config)
logger = logging.getLogger(__name__)

app = Celery(__name__, broker=celery_config.broker, backend=celery_config.backend)
app.config_from_object(celery_config.celeryconfig)

# Автопоиск задач
app.autodiscover_tasks()


# app.autodiscover_tasks(['server.tasks.v1'], related_name='tasks', force=True)


def creating_periodic_tasks() -> None:
    for resource in sites_list:
        app.conf.beat_schedule = {
            'task_bolid_data_collection': {
                'task': resource.task,
                'schedule': crontab(minute=f'*/{celery_config.resources_parsing_time}'),
                'options': {
                    'routing_key': 'task_data_collection',
                    'priority': 10
                },
            },
        }


# При запуске celery выполняем
@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    try:
        celery_type = os.environ.get('CELERY_TYPE')

        if not celery_type == 'FLOWER':
            logger.info('Scheduler registry database')
            database_config: DatabaseConfig = get_database_config()
            registry_database(database_config=database_config)

        if celery_type == 'BEAT':
            # Делаем синхронизацию коллекции с базой данных

            if True:
                # Если синхронизация завершилась успехом, делаем назначенные задачи
                logger.info('Creating scheduled Tasks')
                creating_periodic_tasks()
                logger.info('Scheduled tasks created')

    except Exception as error:
        logger.error(error)
        logger.error(traceback.format_exc(limit=None, chain=True))
        logger.error('Configuration completed with errors')
