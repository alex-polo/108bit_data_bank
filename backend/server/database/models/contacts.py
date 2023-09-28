from sqlalchemy import Table, Column, ForeignKey, Integer

from database.lib import Base

contacts = Table(
    "contacts",
    Base.metadata,
    Column("id", Integer(), primary_key=True),
    Column("address", Integer(), primary_key=True),
    Column("phone_number", Integer(), primary_key=False),
)
