from pyrogram import Client
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
from pyrogram.types import Message


async def is_admin(message: Message) -> bool:
    if not message.from_user:
        return False

    if message.chat.type not in ["group", "supergroup", "channel"]:
        return False

    cl: Client = message._client
    cid: int = message.chat.id
    uid: int = message.from_user.id

    return await is_admin_user(cl, cid, uid)


async def is_admin_user(cl: Client, cid: int, uid: int) -> bool:
    try:
        status = await cl.get_chat_member(chat_id=cid, user_id=uid)
        admin_str = ["creator", "administrator"]
        return status.status in admin_str
    except UserNotParticipant:
        return False
