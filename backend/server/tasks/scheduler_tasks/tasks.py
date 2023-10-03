import logging

from celery import shared_task

logger = logging.getLogger(__name__)


@shared_task
def generate_processing_resources_tasks():
    # В оригинале выбираем список задач из базы данных по базе данных
    logger.info('Create tasks for resources')
