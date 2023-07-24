import asyncio
from aiogram import types
from loader import dp, bot
from keyboards import inline
from utils import string


# Другое
@dp.callback_query_handler(text=["other"])
async def other(call: types.CallbackQuery):
    await bot.edit_message_text(chat_id=call.message.chat.id,
                                text=await string.menu(),
                                message_id=call.message.message_id,
                                disable_web_page_preview=True, reply_markup=await inline.other())


# Как пользоваться ботом?
@dp.callback_query_handler(text=["manual"])
async def manual(call: types.CallbackQuery):
    await bot.edit_message_text(chat_id=call.message.chat.id,
                                text=await string.manual(), parse_mode="MarkdownV2",
                                message_id=call.message.message_id,
                                disable_web_page_preview=True, reply_markup=await inline.backManual())


# Игра
@dp.callback_query_handler(text=["game", "again"])
async def game(call: types.CallbackQuery):
    if call.data != "again":
        await bot.edit_message_text(chat_id=call.message.chat.id,
                                    text="_ℹ️ Если кубик выдаёт значение 1, 2 или 3_\n*_Вы выграли\!💸_*",
                                    parse_mode="MarkdownV2",
                                    message_id=call.message.message_id,
                                    disable_web_page_preview=True)
    else:
        await call.message.delete()

    slot = await bot.send_dice(call.from_user.id, emoji="🎲")

    await asyncio.sleep(4)

    if slot.dice.value <= 3:
        await bot.send_message(call.from_user.id, "_Поздровляю\!_ 🎉\n*_Вы выграли\!_*", parse_mode="MarkdownV2",
                               reply_markup=await inline.game())
    else:
        await bot.send_message(call.from_user.id, "_К сожелению\!_ 😔\n*_Вы проиграли\!_*", parse_mode="MarkdownV2",
                               reply_markup=await inline.game())
