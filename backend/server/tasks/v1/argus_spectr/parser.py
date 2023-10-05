import asyncio
import logging
import traceback

from celery import shared_task

from server.tasks.classes import ReturnedValue, LoaderValue, ErrorValue, ContactsData
from server.tasks.utils import download
from server.tasks.v1.argus_spectr.contacts import contacts_parse
from server.tasks.v1.argus_spectr import urls
from fake_useragent import UserAgent

logger = logging.getLogger(__name__)

useragent = UserAgent()

async def main() -> None:

    headers = {
        'User-Agent': useragent.random
    }

    # Получаем контакты
    contacts: ReturnedValue = await contacts_parse(url=urls.url_contacts, headers=headers)
    print(contacts)
    if contacts.is_success:
        contacts_data: ContactsData = contacts.data
    else:
        error: ErrorValue = contacts.data
        logger.error(error.message)
        if error.traceback is not None:
            logger.error(error.traceback)

    # Получаем категории
    # download_data: ReturnedValue = await download(url=url_products, headers=useragent.random)
    # if download_data.is_success:
    #     data: LoaderValue = download_data.data
    #     logger.info(f'Download Bolid data, response code: {data.response_code}')
    #
    #     # Парсим данные
    #
    #
    #
    # else:
    #     # Пишем ошибку в лог и в базу данных event
    #     data: ErrorValue = download_data.data
    #     logger.error(data.message)
    #     logger.error(data.traceback)


@shared_task()
def task() -> None:
    try:
        logger.info('Running Argus tasks')
        asyncio.run(main())
        logger.info('Argus tasks is finished')
    except Exception as error:
        logger.error(error)
        logger.error(traceback.format_exc(limit=None, chain=True))
