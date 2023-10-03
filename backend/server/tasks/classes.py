from dataclasses import dataclass


@dataclass
class SchemeParser:
    parser: str
    name_task: str
    is_enabled: bool
