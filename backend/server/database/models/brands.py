from datetime import datetime
from xmlrpc.client import Boolean

from sqlalchemy import Table, Column, ForeignKey, Integer, String, Text, DateTime

from database.lib import Base

from backend.server.config import func

brands = Table(
    "brands",
    Base.metadata,
    Column("id", Integer(), primary_key=True),
    Column("brand", String(500), nullable=False),
    Column("field_tag", Integer(), primary_key=True),
    Column("firmware", Integer(), primary_key=True),
    Column("hardware", Integer(), primary_key=True),
    Column("info", Text(), nullable=False),
    Column("support", Integer(), primary_key=True),
    Column("is_enable", Boolean(), primary_key=True),
    Column("created_on", DateTime(), default=datetime.now),
    Column("updated_on", DateTime(), default=datetime.now, onupdate=datetime.now),
    #ИМЯ !?
    # Column("right_id", ForeignKey("right_table.id"), primary_key=True),
)
