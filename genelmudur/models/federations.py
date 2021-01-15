from sqlalchemy import Column
from sqlalchemy.types import BigInteger, Integer
from genelmudur.models.helpers.base import Base


class Federations(Base):
    __tablename__ = "FEDERATIONS"

    id = Column(Integer, primary_key=True, autoincrement=True)
    fed_id = Column(BigInteger)

    def __init__(self, chat_id: int, fed_id: int, fed_name: str):
        self.fed_id = fed_id
        self.fed_name = fed_name
