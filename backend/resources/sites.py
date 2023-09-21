from resources.classes import Resource
from parsers.bolid import bolid_parser

sites_list: list = [
    Resource(
        name='bolid',
        system_name='bolid',
        url='https://bolid.ru',
        tag='#Bolid',
        field_tags=['#Системы_автоматики', '#Системы_безопасности'],
        function=bolid_parser,
        is_enabled=True
    ),
]

# https://macroscop.com/produkty
# Eltys
# https://bolid.ru/production/
# https://rubezh.ru/brands
# https://www.parsec.ru/  !!!!!
# https://www.perco.ru/products/
# https://sigur.com/
# https://ironlogic.ru/il_new.nsf/htm/ru_home
# https://bastion-tech.ru/
# https://argus-spectr.ru/
