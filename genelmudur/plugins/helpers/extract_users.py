from typing import List
from pyrogram.types import Message, User


async def extract_users(msg: Message) -> List[User]:
    total: List[User] = []

    if msg.reply_to_message and msg.reply_to_message.from_user:
        total.append(msg.reply_to_message.from_user)

    if len(mentions := [entity for entity in msg.entities if 'mention' in entity.type]) > 0:
        no_username = [i.user for i in mentions if i.type == 'text_mention']
        total += no_username

        async def get_member(off: int, len: int) -> User:
            mention = msg.text[off:off+len]
            return await msg._client.get_users(user_ids=mention)

        possible_users = [i for i in mentions if i.type == 'mention']
        for nickname in possible_users:
            try:
                total.append(await get_member(nickname.offset, nickname.length))
            except BaseException:
                pass

    if msg.text:
        ids = [int(i) for i in msg.text.split() if i.isdigit()]
        if len(ids):
            for id in ids:
                try:
                    total.append(await msg._client.get_users(user_ids=id))
                except BaseException:
                    pass

    return total
