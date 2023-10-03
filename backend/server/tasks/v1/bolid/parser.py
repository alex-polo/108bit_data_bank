import asyncio
import logging

from celery import shared_task

from server.tasks.classes import ReturnedValue, LoaderValue, ErrorValue
from server.tasks.utils import download
from server.tasks.v1.bolid.urls import url_products
from fake_useragent import UserAgent

logger = logging.getLogger(__name__)

useragent = UserAgent()

async def main() -> None:
    # Скачиваем данные
    download_data: ReturnedValue = await download(url=url_products, headers=useragent.random)
    if download_data.is_success:
        data: LoaderValue = download_data.data
        logger.info(f'Download Bolid data, response code: {data.response_code}')

        # Парсим данные

    else:
        # Пишем ошибку в лог и в базу данных event
        data: ErrorValue = download_data.data
        logger.error(data.message)
        logger.error(data.traceback)


@shared_task()
def task() -> None:
    try:
        logger.info('Running Bolid tasks')
        asyncio.run(main())
        logger.info('Bolid tasks is finished')
    except Exception as error:
        pass

