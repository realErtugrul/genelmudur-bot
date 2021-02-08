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

Created using the example https://docs.pyrogram.org/start/examples/welcomebot
"""
from genelmudur.BotConfig import genelmudur
from genelmudur.utils.target import target_filter
from pyrogram import Client, filters
from pyrogram.types import Chat, Message


@genelmudur.on_message(target_filter() & filters.new_chat_members)
async def new_member(client: Client, message: Message) -> None:
    """
    Sends welcome message when new members join the group
    """
    # Build the new members list (with mentions) by using their first_name
    # MENTION = "[{}](tg://user?id={})"
    new_members_list = [u.mention for u in message.new_chat_members]

    # Get name of the group or channel
    group_name = message.chat.title

    # Join new members to a single string
    new_members = ", ".join(new_members_list)

    # Welcome message, hard coded atm, has to be outsourced to database
    text = f"Merhaba {new_members}, {group_name} Grubuna hoş geldin!"

    # Send the welcome message, without the web page preview
    await message.reply_text(text, disable_web_page_preview=True)


async def set_welcome():
    """
    Specify the settings of the welcome function
    """
    pass
