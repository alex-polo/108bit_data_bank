from bs4 import BeautifulSoup
import requests
from server.tasks.v1.bolid.urls import url_contacts
from fake_useragent import UserAgent

useragent = UserAgent()

def contacts_parse():
    url = url_contacts
    headers = useragent.random

    responce = requests.get(url, headers=headers)
    soup = BeautifulSoup(responce.content, 'html.parser')
    items = soup.findall('div', class_='address')
    contacts = []

    for item in items:
        contacts.append({
            'title': item.find('span', class_='addressRegion').get_text(strip = True)
        })

    for contact in contacts:
        print(contact['title'])

contacts_parse()


