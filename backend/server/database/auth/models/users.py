from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import Integer, Column

from server.database.lib import Base


class Users(SQLAlchemyBaseUserTable[int], Base):
    id = Column(Integer, primary_key=True)
