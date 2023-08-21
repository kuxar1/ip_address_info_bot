from aiogram import types

kb = [
    [types.KeyboardButton(text="Enter IP address")]
]
keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True, is_persistent=True)
