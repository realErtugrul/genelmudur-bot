"""
genelmudur-bot - Another Telegram group management bot.
Copyright (C) 2020-2021 realErtugrul <https://github.com/realErtugrul>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
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
