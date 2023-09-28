from sqlalchemy import Table, Column, ForeignKey

from database.lib import Base

processing_errors = Table(
    "processing_errors",
    Base.metadata,
    Column("left_id", ForeignKey("left_table.id"), primary_key=True),
)
