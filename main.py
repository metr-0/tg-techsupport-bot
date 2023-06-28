import logging
import json

from aiogram import Bot, Dispatcher, executor, types

logging.basicConfig(level=logging.INFO)

with open('config.json') as config_file:
    config = json.load(config_file)

bot = Bot(token=config['token'])
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def welcome(message: types.Message):
    await message.reply("Hello World!")


@dp.message_handler(lambda message: message.chat.type == 'private')
async def question(message: types.Message):
    await message.forward(
        chat_id=config['chatId']
    )
    await message.reply('Forwarded!')


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


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
