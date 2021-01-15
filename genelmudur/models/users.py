from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import BigInteger, String, Integer
from genelmudur.models.helpers.base import Base


class Users(Base):
    __tablename__ = "USERS"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger)
    username = Column(String(100), nullable=True)

    def __init__(self, user_id: int, username: str):
        self.user_id = user_id
        self.username = username
