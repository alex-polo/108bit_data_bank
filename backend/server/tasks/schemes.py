from typing import List

from server.tasks.classes import SchemeParser

parser_list: List[SchemeParser] = [
    SchemeParser(
        parser='server.tasks.v1.bolid.parser.task',
        name_task='bolid_parser_v1',
        is_enabled=True
    ),
    # (
    #     parser='server.tasks.v1.bolid.parser.task',
    #     name_task='bolid_parser_v1',
    #     is_enabled=True
    # ),
]
