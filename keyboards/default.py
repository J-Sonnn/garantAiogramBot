from aiogram import types
from aiogram.types import ReplyKeyboardMarkup

remove = types.ReplyKeyboardRemove()


async def back():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add('Назад ↩')
    return keyboard
