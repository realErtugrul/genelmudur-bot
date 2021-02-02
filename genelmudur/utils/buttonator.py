"""
genelmudur-bot - Another Telegram group management bot.
Copyright (C) 20202021 realErtugrul <https://github.com/realErtugrul>

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
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def slicer(button_list: list, size: int) -> list:
    return [button_list[i : i + size] for i in range(0, len(button_list), size)]


def button_maker(buttons: dict, size: int) -> InlineKeyboardMarkup:
    buttons = [
        InlineKeyboardButton(text=v, callback_data=k) for k, v in buttons.items()
    ]
    buttons = slicer(buttons, size)

    return InlineKeyboardMarkup(buttons)
