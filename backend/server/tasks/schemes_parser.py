from typing import List

from server.tasks.classes import SchemeParser

parser_list: List[SchemeParser] = [
    SchemeParser(
        parser='server.tasks.v1.bolid.parser.task',
        is_enabled=True
    )
]
