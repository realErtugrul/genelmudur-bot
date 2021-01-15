from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import BigInteger, String, Integer
from genelmudur.models.helpers.base import Base


class Users(Base):
    __tablename__ = "USERS"

    id = Column(Integer, primary_key=True, autoincrement=True)
    uid = Column(BigInteger)
    username = Column(String(100), nullable=True)

    def __init__(self, uid: int, username: str):
        self.uid = uid
        self.username = username
