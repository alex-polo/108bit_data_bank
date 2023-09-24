from typing import Optional, AsyncGenerator

import sqlalchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    async_sessionmaker,
    AsyncSession,
    create_async_engine,
    AsyncAttrs
)

from server.config import DatabaseConfig

_engine: AsyncEngine = Optional[None]
_async_session_maker: async_sessionmaker = Optional[None]


class Base(AsyncAttrs, DeclarativeBase):
    pass


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with _async_session_maker() as session:
        yield session


def get_metadata() -> MetaData:
    return Base.metadata


def registry_database(database_config: DatabaseConfig) -> str:
    global _engine, _async_session_maker

    database_url = f'postgresql+asyncpg://' \
                   f'{database_config.db_user}:' \
                   f'{database_config.db_pass}@' \
                   f'{database_config.db_host}:' \
                   f'{database_config.db_port}/' \
                   f'{database_config.db_name}'

    _engine = create_async_engine(database_url)
    _async_session_maker = async_sessionmaker(_engine, class_=AsyncSession, expire_on_commit=False)

    return sqlalchemy.__version__
