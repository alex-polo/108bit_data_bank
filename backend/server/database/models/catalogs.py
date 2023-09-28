from sqlalchemy import Table, Column, ForeignKey

from database.lib import Base

catalogs= Table(
    "catalogs",
    Base.metadata,
    Column("firmware", ForeignKey("left_table.id"), primary_key=True),
    Column("software", ForeignKey("right_table.id"), primary_key=True),
)