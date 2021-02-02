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
from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import BigInteger, Integer, String


class Users(Base):
    __tablename__ = "USERS"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger)
    username = Column(String(100), nullable=True)

    def __init__(self, user_id: int, username: str):
        self.user_id = user_id
        self.username = username
