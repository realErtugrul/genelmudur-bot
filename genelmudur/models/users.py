from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import BigInteger, String, Integer
from genelmudur.models.helpers.base import Base


class Users(Base):
    __tablename__ = "USERS"

    id = Column(Integer, primary_key=True, autoincrement=True)
    uid = Column(BigInteger)
    chat_id = Column(Integer)
    username = Column(String(100), nullable=True)

    def __init__(self, uid: int, chat_id: int, username: str):
        self.uid = uid
        self.chat_id = chat_id
        self.username = username