from typing import Optional, AsyncGenerator

import sqlalchemy
from sqlalchemy import MetaData, String, Integer
from sqlalchemy.ext.asyncio import AsyncEngine, async_sessionmaker, AsyncSession, create_async_engine, AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from config.classes import DatabaseConfig

_engine: AsyncEngine = Optional[None]
_async_session_maker: async_sessionmaker = Optional[None]


class Base(AsyncAttrs, DeclarativeBase):
    pass


# class Sites(Base):
#     __tablename__ = 'sites'
#
#     id: Mapped[int] = mapped_column(primary_key=True)
#     system_name: Mapped[String] = mapped_column(String(255), nullable=False, unique=True)

class User(Base):
    __tablename__ = "user"

    id = mapped_column(Integer, primary_key=True)
    name: Mapped[str]

metadata: MetaData = Base.metadata
print(metadata.tables)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with _async_session_maker() as session:
        yield session


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
