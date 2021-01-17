import time

from genelmudur.BotConfig import genelmudur
from genelmudur.utils.prefix import cmdprefix
from pyrogram.types import Message


@genelmudur.on_message(cmdprefix("ping"))
async def ping(_, message: Message):
    start = time.time()
    reply = await message.reply_text("...")
    delta_ping = time.time() - start
    await reply.edit_text(f"**Pong!** `{delta_ping * 1000:.3f} ms`")
