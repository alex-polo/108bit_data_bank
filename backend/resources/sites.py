from typing import List

from resources.classes import Resource

sites_list: List[Resource] = [
    Resource(
        name='bolid',
        system_name='bolid',
        url='https://bolid.ru',
        tag='#Bolid',
        field_tags=['#Системы_автоматики', '#Системы_безопасности'],
        task='server.tasks.v1.bolid.parser.task',
        is_enabled=True
    ),
    Resource(
        name='macroscop',
        system_name='macroscop',
        url='https://macroscop.com',
        tag='#Macroscop',
        field_tags=['#Системы_автоматики', '#Системы_безопасности'],
        task='server.tasks.v1.macroscop.parser.task',
        is_enabled=True
    ),
    Resource(
        name='rubezh',
        system_name='rubezh',
        url='https://rubezh.ru',
        tag='#Rubezh',
        field_tags=['#Системы_автоматики', '#Системы_безопасности'],
        task='server.tasks.v1.rubezh.parser.task',
        is_enabled=True
    ),
    Resource(
        name='parsec',
        system_name='parsec',
        url='https://parsec.ru',
        tag='#Parsec',
        field_tags=['#Системы_автоматики', '#Системы_безопасности'],
        task='server.tasks.v1.parsec.parser.task',
        is_enabled=True
    ),
    Resource(
        name='perco',
        system_name='perco',
        url='https://perco.ru',
        tag='#Perco',
        field_tags=['#Системы_автоматики', '#Системы_безопасности'],
        task='server.tasks.v1.perco.parser.task',
        is_enabled=True
    ),
    Resource(
        name='sigur',
        system_name='sigur',
        url='https://sigur.com',
        tag='#Sigur',
        field_tags=['#Системы_автоматики', '#Системы_безопасности'],
        task='server.tasks.v1.sigur.parser.task',
        is_enabled=True
    ),
    Resource(
        name='ironlogic',
        system_name='ironlogic',
        url='https://ironlogic.ru',
        tag='#Ironlogic',
        field_tags=['#Системы_автоматики', '#Системы_безопасности'],
        task='server.tasks.v1.ironlogic.parser.task',
        is_enabled=True
    ),
    Resource(
        name='bastion',
        system_name='bastion',
        url='https://bastion-tech.ru',
        tag='#Bastion',
        field_tags=['#Системы_автоматики', '#Системы_безопасности'],
        task='server.tasks.v1.bastion.parser.task',
        is_enabled=True
    ),
    Resource(
        name='argus',
        system_name='argus',
        url='https://argus-spectr.ru',
        tag='#Argus',
        field_tags=['#Системы_автоматики', '#Системы_безопасности'],
        task='server.tasks.v1.argus.parser.task',
        is_enabled=True
    ),
]

# Eltys
