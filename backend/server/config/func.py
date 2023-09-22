import os

from environs import Env

from etc.server_settings import ALLOW_CREDENTIALS, ALLOW_METHODS, ALLOW_HEADERS, LOGGING_CONFIG as SERVER_LOGGING_CONFIG
from etc.tasks_settings import CELERY_CONFIG, LOGGING_CONFIG as CELERY_LOGGING_CONFIG, RESOURCES_PARSING_TIME
from server.config.classes import DatabaseConfig, ServerAPIConfig, CeleryConfig


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
        allow_headers=ALLOW_HEADERS,
        logging_config=os.path.join('etc', SERVER_LOGGING_CONFIG)
    )


def get_celery_config() -> CeleryConfig:
    env = Env()
    env.read_env(os.path.join(os.getcwd(), '.env'))

    return CeleryConfig(
        broker=env.str('CELERY_BROKER'),
        backend=env.str('CELERY_BACKEND'),
        celeryconfig=f'etc.{CELERY_CONFIG}',
        logging_config=os.path.join('etc', CELERY_LOGGING_CONFIG),
        resources_parsing_time=RESOURCES_PARSING_TIME
    )
