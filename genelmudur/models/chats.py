from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import BigInteger, Integer
from genelmudur.models.helpers.base import Base
from sqlalchemy.orm import relationship


class Chats(Base):
    __tablename__ = "CHAT_TABLE"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("Users.id"))
    cid = Column(BigInteger)
    warnings = Column(Integer, nullable=True, default=0)
    chat = relationship("Users")

    def __init__(
        self,
        cid,
        uid,
        cname,
    ):
        self.uid = uid
        self.cid = cid
        self.cname = cname