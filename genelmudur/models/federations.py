from genelmudur.models.helpers.base import Base
from sqlalchemy import Column
from sqlalchemy.types import JSON, BigInteger, Integer, String


class Federations(Base):
    __tablename__ = "FEDERATIONS"

    id = Column(Integer, primary_key=True, autoincrement=True)
    fed_id = Column(BigInteger)
    fed_name = Column(String(100))
    fed_owner = Column(BigInteger)
    fed_admins = Column(JSON, nullable=True)

    def __init__(self, chat_id: int, fed_id: int, fed_name: str, fed_owner: int):
        self.fed_id = fed_id
        self.fed_name = fed_name
        self.fed_owner = fed_owner
