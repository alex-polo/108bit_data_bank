from datetime import datetime
from typing import List
from xmlrpc.client import Boolean

from sqlalchemy import Integer, func
from sqlalchemy.orm import Mapped, mapped_column

from sqlalchemy import Table, Column, ForeignKey, Integer, String, Text, DateTime

from server.database.lib import Base


class Brands(Base):
    __tablename__ = "brands"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[String] = mapped_column(String(500), nullable=False)
    field_tags: Mapped[List[]] = mapped_column(nullable=True)
    firmware_catalog: Mapped
    hardware_catalog: Mapped

    created_on: Mapped[DateTime] = mapped_column(DateTime(), default=func.now()),
    update_on: Mapped[DateTime] = mapped_column(DateTime(), default=func.now(), onupdate=func.now()),

brands = Table(
    "brands",
    Base.metadata,
    Column("field_tag", Integer()),
    # Column("firmware", Integer(), primary_key=True),
    # Column("hardware", Integer(), primary_key=True),
    Column("contacts", Integer(), primary_key=True),
    Column("is_enable", Boolean(), primary_key=True),
    #ИМЯ !?
    # Column("right_id", ForeignKey("right_table.id"), primary_key=True),
)
