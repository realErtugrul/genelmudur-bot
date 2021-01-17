from genelmudur.models.helpers.base import Base
from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import BigInteger, Integer, String


class Chats(Base):
    __tablename__ = "CHATS"

    id = Column(Integer, primary_key=True, autoincrement=True)
    chat_id = Column(BigInteger)
    chat_name = Column(String(100), nullable=True)
    federation = Column(Integer, nullable=True)

    def __init__(self, chat_id: int, chat_name: str, federation: int):
        self.chat_id = chat_id
        self.chat_name = chat_name
        self.federation = federation
