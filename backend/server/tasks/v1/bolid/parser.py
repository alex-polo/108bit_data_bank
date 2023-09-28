from celery import shared_task
import requests
from bs4 import BeautifulSoup

from server.tasks.v1.bolid.contacts import contacts_parse
from server.tasks.v1.bolid.urls import url_contacts


@shared_task()
def task() -> None:
    # Парсим контакты
    contacts = contacts_parse(url=url_contacts)

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
