from typing import Optional, AsyncGenerator

import sqlalchemy
from sqlalchemy import String
from sqlalchemy.ext.asyncio import AsyncEngine, async_sessionmaker, AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped

from server.config import DatabaseConfig

_engine: AsyncEngine = Optional[None]
_async_session_maker: async_sessionmaker = Optional[None]


class Base(DeclarativeBase):
    pass


class Sites(Base):
    __tablename__ = "sites"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    fullname: Mapped[Optional[str]]


# async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
#     async with _async_session_maker() as session:
#         yield session
#
#
# def registry_database(database_config: DatabaseConfig) -> str:
#     global _engine, _async_session_maker
#
#     database_url = f'postgresql+asyncpg://' \
#                    f'{database_config.db_user}:' \
#                    f'{database_config.db_pass}@' \
#                    f'{database_config.db_host}:' \
#                    f'{database_config.db_port}/' \
#                    f'{database_config.db_name}'
#
#     _engine = create_async_engine(database_url)
#     _async_session_maker = async_sessionmaker(_engine, class_=AsyncSession, expire_on_commit=False)
#
#     return sqlalchemy.__version__
