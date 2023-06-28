from bot import dp

from aiogram import types


@dp.message_handler(commands=['ping'])
async def ping(message: types.Message):
    await message.reply("pong")
