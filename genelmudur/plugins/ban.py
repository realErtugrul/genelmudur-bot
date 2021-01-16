from genelmudur.plugins.helpers.extract_user import extract_users
from genelmudur.plugins.helpers.admin_check import is_admin, is_admin_user
from pyrogram.types import Message
from genelmudur.BotConfig import genelmudur
from genelmudur.utils.prefix import cmdprefix


@genelmudur.on_message(cmdprefix("ban"))
async def ban(_, message: Message):
    if not await is_admin_user(message._client, message.chat.id, (await message._client.get_me()).id):
        await message.reply('I\'m not admin!')
        return

    if not await is_admin(message):
        await message.reply('You\'re not admin!')
        return

    try:
        users = await extract_users(message)
    except BaseException as e:
        print(e)
        users = []

    if len(users) < 1:
        await message.reply('Please specify user(s) to ban by reply, username or user id')
        return

    chat = message.chat
    banned = []
    for user in users:
        if not await is_admin_user(message._client, message.chat.id, user.id):
            try:
                await chat.kick_member(user.id)
                banned.append(user)
            except BaseException as e:
                print(e)

    if len(banned) > 0:
        await message.reply(f'{", ".join([user.mention() for user in banned])} banned!')
    else:
        await message.reply('Ban failed')
