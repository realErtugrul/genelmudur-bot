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
