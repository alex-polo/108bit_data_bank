from dataclasses import dataclass


@dataclass
class ServerAPIConfig:
    host: str
    port: int
    allow_origins: list[str]
    allow_credentials: bool
    allow_methods: list[str]
    allow_headers: list[str]


@dataclass
class DatabaseConfig:
    db_user: str
    db_pass: str
    db_host: str
    db_port: str
    db_name: str
