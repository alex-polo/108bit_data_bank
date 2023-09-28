from dataclasses import dataclass


@dataclass
class SchemeParser:
    parser: str
    is_enabled: bool
