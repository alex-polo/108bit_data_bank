from sqlalchemy import Table, Column, ForeignKey, Integer

from database.lib import Base

categories = Table(
    "categories",
    Base.metadata,
    Column("id", Integer(), primary_key=True),
    Column("right_id", ForeignKey("right_table.id"), primary_key=True),
    Column("right_id", ForeignKey("right_table.id"), primary_key=True),
    Column("right_id", ForeignKey("right_table.id"), primary_key=True),
    Column("right_id", ForeignKey("right_table.id"), primary_key=True),
)
