from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, InputFile
from aiogram.utils.markdown import hcode, hbold

from tgbot.config import load_config


async def start_bot(message: types.Message):
    await message.answer(f"Hello, user!")


async def help(message: types.Message):
    await message.answer()