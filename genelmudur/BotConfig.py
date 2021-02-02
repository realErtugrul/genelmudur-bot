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
from pyrogram import Client
from pyrogram.types import Message


class genelmudur(Client, Message):
    def __init__(self):
        moduleName = "genelmudur"
        name = self.__class__.__name__.lower()
        super().__init__(
            session_name=name,
            config_file=f"{moduleName}/{name}.ini",
            workers=8,
            plugins=dict(root=f"{moduleName}/plugins"),
        )

    async def start(self):
        await super().start()

    async def stop(self, *args):
        await super().stop()
