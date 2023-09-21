import os

from environs import Env

from etc.settings_api_server import ALLOW_CREDENTIALS, ALLOW_METHODS, ALLOW_HEADERS
from server.config.classes import DatabaseConfig, ServerAPIConfig


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


def get_api_server_config() -> ServerAPIConfig:
    env = Env()
    env.read_env(os.path.join(os.getcwd(), '.env'))

    return ServerAPIConfig(
        host=env.str('HOST'),
        port=int(env.str('PORT')),
        allow_origins=env.str('ALLOWED_HOSTS').split(','),
        allow_credentials=ALLOW_CREDENTIALS,
        allow_methods=ALLOW_METHODS,
        allow_headers=ALLOW_HEADERS
    )
