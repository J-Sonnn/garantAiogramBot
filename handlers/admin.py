from aiogram import types
from loader import dp, bot
from database import DB
from keyboards import inline
from utils import string
import config


# Команды бота для админа/главного админа
@dp.message_handler(commands=["botinfo"])
async def botinfo(call: types.CallbackQuery):
    if call.from_user.id == config.mainAdmin:
        await bot.send_message(call.from_user.id, await string.botinfoMain())
    else:
        await bot.send_message(call.from_user.id, await string.botinfo())


# Добавить админа
@dp.message_handler(commands=["addadmin"])
async def addadmin(message: types.Message):
    if message.from_user.id in await DB.selectAllUserFrom('admin'):
        await DB.addAdmin(message.text.replace("/addadmin", ""))
        await bot.send_message(message.from_user.id, 'Успешно! ✅', reply_markup=await inline.back())


# Удалить админа
@dp.message_handler(commands=["delateadmin"])
async def delateadmin(message: types.Message):
    if message.from_user.id in await DB.selectAllUserFrom('admin'):
        await DB.delateAdmin(message.text.replace("/delateadmin ", ""))
        await bot.send_message(message.from_user.id, 'Успешно! ✅', reply_markup=await inline.back())


# Рассылка
@dp.message_handler(commands=["send"])
async def send(message: types.Message):
    if message.from_user.id in await DB.selectAllUserFrom('admin'):
        for i in await DB.selectAllUserFrom('user'):
            try:
                await bot.send_message(i, text=message.text.replace("/send", ""))
            except:
                pass


# Добавление количества человек в бота
@dp.message_handler(commands=["add"])
async def add(message: types.Message):
    if message.from_user.id in await DB.selectAllUserFrom('admin'):
        await DB.updateUserQuantity(int(message.text.replace("/add ", "")) + await DB.selectUserQuantity())
        await bot.send_message(message.from_user.id, 'Успешно! ✅', reply_markup=await inline.back())


# Добавление баланса
@dp.message_handler(commands=["TON", "USDT", "BUSD", "USDC"])
async def addBalance(message: types.Message):
    if message.from_user.id in await DB.selectAllUserFrom('admin'):
        await DB.updateBalance(message.from_user.id, message.text.split()[0].replace("/", ""), message.text.split()[1])
        await bot.send_message(message.from_user.id, 'Успешно! ✅', reply_markup=await inline.back())


# Удаление баланса
@dp.message_handler(commands=["delateTON", "delateUSDT", "delateBUSD", "delateUSDC"])
async def delateBalance(message: types.Message):
    if message.from_user.id in await DB.selectAllUserFrom('admin'):
        await DB.updateBalance(message.from_user.id, message.text.split()[0].replace("/delate", ""), 0)
        await bot.send_message(message.from_user.id, 'Успешно! ✅', reply_markup=await inline.back())
