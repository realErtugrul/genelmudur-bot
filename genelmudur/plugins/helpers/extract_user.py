from typing import List
from pyrogram.types import Message, User


async def extract_users(msg: Message) -> List[User]:
    total = []

    if msg.reply_to_message and msg.reply_to_message.from_user:
        total.append(msg.reply_to_message.from_user)

    if len(mentions := [entity for entity in msg.entities if 'mention' in entity.type]) > 0:
        no_username = [i.user for i in mentions if i.type == 'text_mention']

        async def get_member(off: int, len: int) -> User:
            mention = msg.text[off:off+len]
            return await msg._client.get_users(user_ids=mention)

        username = [(await get_member(i.offset, i.length)) for i in mentions if i.type == 'mention']

        total += no_username + username

    if msg.text:
        ids = [int(i) for i in msg.text.split() if i.isdigit()]
        if len(ids):
            users_ids = await msg._client.get_users(user_ids=ids)
            total += users_ids

    if len(total) < 1:
        raise Exception('User extraction failed')

    return total
