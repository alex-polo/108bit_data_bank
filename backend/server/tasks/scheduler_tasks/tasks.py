import logging

from celery import shared_task

from server.tasks.main import app
from server.tasks.schemes import parser_list

logger = logging.getLogger(__name__)
# from server.tasks.v1.bolid.parser import task as bolid_task
from server.tasks.v1.argus_spectr.parser import task as argus_task


@shared_task
def generate_processing_resources_tasks():
    # В оригинале выбираем список задач из базы данных по базе данных
    logger.info('Create tasks for resources')
    # bolid_task.delay()
    argus_task.delay()
