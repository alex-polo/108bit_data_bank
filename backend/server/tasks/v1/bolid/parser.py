import asyncio
import logging

from celery import shared_task

from server.tasks.classes import ReturnedValue, LoaderValue, ErrorValue
from server.tasks.utils import download
from server.tasks.v1.bolid.urls import url_products

logger = logging.getLogger(__name__)


async def main() -> None:
    # Скачиваем данные
    download_data: ReturnedValue = await download(url=url_products, headers={})
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

# Парсим страничку целиком в файлик

# url = "https://bolid.ru/production/"
#
# headers = {
#     "Accept": "*/*",
#     "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
# }
#
# req = requests.get (url, headers=headers)
# src = req.text
# # print(src)
#
# with open("index.html", "w") as file:
#     file.write(src)

#
#
# with open("index.html") as file:
#     src = file.read()
#
# soup = BeautifulSoup(src, "lxml")
# all_products_hrefs = soup.find_all(class_="menu_left")
# for item in all_products_hrefs:
#     item_text = item.text
#     item_href = item.get("href")
#     print(f"{item.text}: {item_href}")
#


# https://bolid.ru/production/orion/    #Общая инфа
# https://bolid.ru/production/orion/po-orion/ #ПО
# https://bolid.ru/production/orion/po-orion/po-arm/ #ПО АРМ
# https://bolid.ru/production/orion/po-orion/po-config/ #Конфигурирование
# https://bolid.ru/production/orion/po-orion/po-config/pprog.html
# https://bolid.ru/production/orion/po-orion/po-integration/ #ПО интеграция
