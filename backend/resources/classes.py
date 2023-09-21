from dataclasses import dataclass
from typing import Any, List


@dataclass
class Resource:
    name: str
    system_name: str
    tag: str
    field_tags: List[str]
    # url: str
    function: Any
    is_enabled: bool
