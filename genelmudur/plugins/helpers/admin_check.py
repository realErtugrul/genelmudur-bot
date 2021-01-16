from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
from pyrogram.types import Message
from pyrogram import Client


async def is_admin(msg: Message) -> bool:
    if not msg.from_user:
        return False

    if msg.chat.type not in ["group", "supergroup", "channel"]:
        return False

    cl: Client = msg._client
    cid: int = msg.chat.id
    uid: int = msg.from_user.id

    return await is_admin_user(cl, cid, uid)


async def is_admin_user(cl: Client, cid: int, uid: int) -> bool:
    try:
        status = await cl.get_chat_member(chat_id=cid, user_id=uid)
        admin_str = ["creator", "administrator"]
        return status.status in admin_str
    except UserNotParticipant:
        return False
