from sqlalchemy import Table, Column, ForeignKey, Integer

from server.database.lib import Base
from sqlalchemy.orm import Mapped, mapped_column


class Contacts(Base):
    __tablename__ = "contacts"

    address: Mapped[Text] = mapped_column(Integer, primary_key=True)
    phones: Mapped[Text] = mapped_column(String(500), nullable=False)
    mail: Mapped[Text] = mapped_column()
    support: Mapped[Text] = mapped_column(String(50), nullable=True)