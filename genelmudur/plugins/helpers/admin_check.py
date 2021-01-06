from pyrogram.types import Message
from pyrogram import Client


async def is_admin(msg: Message) -> bool:
    if not msg.from_user:
        return False

    if msg.chat.type not in ["supergroup", "channel"]:
        return False

    cl: Client = msg._client
    cid: int = msg.chat.id
    uid: int = msg.from_user.id

    status = await cl.get_chat_member(chat_id=cid, user_id=uid)
    admin_str = ["creator", "administrator"]
    return True if status.status not in admin_str else False