from bot import bot, dp, config

from aiogram import types


@dp.message_handler(commands=['ping'])
async def ping(message: types.Message):
    await message.reply("pong")
