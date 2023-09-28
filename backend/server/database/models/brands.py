from xmlrpc.client import Boolean

from sqlalchemy import Table, Column, ForeignKey, Integer

from database.lib import Base

from backend.server.config import func

brands = Table(
    "brands",
    Base.metadata,
    Column("id", Integer(), primary_key=True),
    Column("brand", Integer(), primary_key=True),
    Column("created_date", Integer(), primary_key=False,default=func.now),
    Column("field_tag", Integer(), primary_key=True),
    Column("firmware", Integer(), primary_key=True),
    Column("hardware", Integer(), primary_key=True),
    Column("info", Integer(), primary_key=True),
    Column("support", Integer(), primary_key=True),
    Column("is_enable", Boolean(), primary_key=True),
    #ИМЯ !?
    # Column("right_id", ForeignKey("right_table.id"), primary_key=True),
)
