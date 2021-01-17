from genelmudur.models.helpers.base import Base
from sqlalchemy import Column, ForeignKey
from sqlalchemy.sql.sqltypes import JSON
from sqlalchemy.types import BigInteger, Integer


class Memberships(Base):
    __tablename__ = "MEMBERSHIPS"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("Users.id"))
    chat_id = Column(BigInteger, ForeignKey("Chats.id"))
    actions = Column(JSON, nullable=True)

    def __init__(self, user_id: int, chat_id: int, chat_name: str, actions: str):
        self.user_id = user_id
        self.chat_id = chat_id
        self.chat_name = chat_name
        self.actions = actions
