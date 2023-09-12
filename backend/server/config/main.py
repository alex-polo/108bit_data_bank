import os

from environs import Env

from server.config.classes import DatabaseConfig


def get_database_config() -> DatabaseConfig:
    env = Env()
    env.read_env(os.path.join(os.getcwd(), '.env'))

    return DatabaseConfig(
        db_user=env.str('DB_USER'),
        db_pass=env.str('DB_PASS'),
        db_host=env.str('DB_HOST'),
        db_port=env.str('DB_PORT'),
        db_name=env.str('DB_NAME'),
    )
