from sqlalchemy import Table, Column, ForeignKey

from database.lib import Base

association_table = Table(
    "categories",
    Base.metadata,
    Column("left_id", ForeignKey("left_table.id"), primary_key=True),
    Column("right_id", ForeignKey("right_table.id"), primary_key=True),
    Column("right_id", ForeignKey("right_table.id"), primary_key=True),
    Column("right_id", ForeignKey("right_table.id"), primary_key=True),
    Column("right_id", ForeignKey("right_table.id"), primary_key=True),
)
