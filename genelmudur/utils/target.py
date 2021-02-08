"""
genelmudur-bot - Another Telegram group management bot.
Copyright (C) 2021 realErtugrul <https://github.com/realErtugrul>

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
from functools import partial

from pyrogram import filters

TARGET = [-375226089, -1001139574198]
# Bot Test, Genel Sohbet

# Predefined filter, to filter messages from chats in the constant (list) TARGET
target_filter = partial(filters.chat, TARGET)
