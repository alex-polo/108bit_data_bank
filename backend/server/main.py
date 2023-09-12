from config import get_database_config
from server import database as database


def run() -> None:
    config = get_database_config()
    print(database.registry_database(database_config=config))
