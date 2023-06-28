from bot import bot, dp, config

from aiogram import types


@dp.message_handler(commands=['start', 'help'])
async def signup(message: types.Message):
    await message.reply("Hello World!")
