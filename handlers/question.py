from bot import bot, dp, config

from aiogram import types


@dp.message_handler(lambda message: message.chat.type == 'private')
async def question(message: types.Message):
    await message.forward(
        chat_id=config['chatId']
    )
    await message.reply('Forwarded!')
