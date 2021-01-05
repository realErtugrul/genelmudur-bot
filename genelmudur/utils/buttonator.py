from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def slicer(button_list: list, size: int) -> list:
    return [button_list[i : i + size] for i in range(0, len(button_list), size)]


def button_maker(buttons: dict, size: int) -> InlineKeyboardMarkup:
    buttons = [
        InlineKeyboardButton(text=v, callback_data=k) for k, v in buttons.items()
    ]
    buttons = slicer(buttons, size)

    return InlineKeyboardMarkup(buttons)
