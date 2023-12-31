import logging

from celery import shared_task

from server.tasks.main import app
from server.tasks.schemes import parser_list

logger = logging.getLogger(__name__)
# from server.tasks.v1.bolid.parser import task as bolid_task
# from server.tasks.v1.argus_spectr.parser import task as argus_task #!!!!!!!!!!!!
# from server.tasks.v1.bastion_tech.parser import task as bastion_task #!!!!!!!!!!!!
# from server.tasks.v1.ironlogic.parser import task as ironlogic_task
# from server.tasks.v1.macroscop.parser import task as macroscop_task
from server.tasks.v1.parsec.parser import task as parsec_task

@shared_task
def generate_processing_resources_tasks():
    # В оригинале выбираем список задач из базы данных по базе данных
    logger.info('Create tasks for resources')
    # bolid_task.delay()
    # argus_task.delay()
    # bastion_task.delay()
    # ironlogic_task.delay()
    # macroscop_task.delay()
    parsec_task.delay()