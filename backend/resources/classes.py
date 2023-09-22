from dataclasses import dataclass
from typing import Any, List


@dataclass
class Resource:
    name: str
    system_name: str
    url: str
    tag: str
    field_tags: List[str]
    task: str
    is_enabled: bool
