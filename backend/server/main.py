from fastapi import FastAPI

from server.config import get_database_config, ServerAPIConfig
from server import database as database

origins = [
    "http://localhost:5173",
    "http://localhost:3000",
]

api_server = FastAPI()


def run(config_server: ServerAPIConfig = None) -> None:
    config = get_database_config()
    print(database.registry_database(database_config=config))
