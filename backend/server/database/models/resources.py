from sqlalchemy.orm import Mapped, mapped_column

from server.database.lib import Base


class Resources(Base):
    __tablename__ = "resources"

    id: Mapped[int] = mapped_column(primary_key=True)
