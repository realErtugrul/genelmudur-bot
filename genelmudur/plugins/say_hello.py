import asyncio
import time
from functools import partial

from genelmudur.BotConfig import genelmudur
from genelmudur.utils import buttonator
from genelmudur.utils.prefix import cmdprefix
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, Message


@genelmudur.on_message(cmdprefix("start"))
async def say_hello(client: Client, message: Message) -> None:
    msg = await message.reply_text(text="`Hello..`", quote=True)
    await asyncio.sleep(1)
    await msg.edit_text(text="`Hello I'm Ready to Use`")


@genelmudur.on_message(cmdprefix("ping"))
async def ping(_, message: Message):
    start = time.time()
    reply = await message.reply_text("...")
    delta_ping = time.time() - start
    await reply.edit_text(f"**Pong!** `{delta_ping * 1000:.3f} ms`")


my_buttons = {
    "Button1": "Button1",
    "Button2": "Button2",
    "Button3": "Button3",
    "Button4": "Button4",
    "Button5": "Button5",
}
button_filter = filters.create(lambda _, __, query: query.data in my_buttons.keys())


@genelmudur.on_message(cmdprefix("buttons"))
async def buttons(client: Client, message: Message):
    me = await client.get_me()

    if me.is_bot:
        await message.reply_text(
            text="These are test buttons with callback",
            reply_markup=buttonator.button_maker(buttons=my_buttons, size=2),
        )

    else:
        await message.reply_text(
            text="Users can not send `keyboard markup`. **I'm sorry..**",
        )


@genelmudur.on_callback_query(button_filter)
async def reply_callback(_: Client, callback=CallbackQuery):
    await callback.message.reply_text(text=callback.data)
