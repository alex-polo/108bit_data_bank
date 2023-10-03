from dataclasses import dataclass
from typing import Union


@dataclass
class SchemeParser:
    parser: str
    name_task: str
    is_enabled: bool


@dataclass
class ErrorValue:
    message: str
    traceback: Union[str, None]


@dataclass
class LoaderValue:
    response_code: int
    content: str


@dataclass
class CategoryData:
    pass


@dataclass
class ReturnedValue:
    is_success: bool
    data: Union[ErrorValue, LoaderValue]
