from bot import bot, dp, config

from aiogram import types


@dp.message_handler(lambda message: message.chat.id == config['chatId'] and
                    message.reply_to_message and message.reply_to_message.forward_from)
async def answer(message: types.Message):
    user_id = message.reply_to_message.forward_from.id
    await bot.send_message(
        chat_id=user_id,
        text=message.text,
        reply_to_message_id=message.reply_to_message.forward_from_message_id
    )
    await message.reply('Sent!')
