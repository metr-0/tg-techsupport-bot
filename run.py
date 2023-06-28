import logging
import json

from aiogram import Bot, Dispatcher, executor, types

logging.basicConfig(level=logging.INFO)

with open('config.json') as config_file:
    config = json.load(config_file)

bot = Bot(token=config['token'])
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hello World!")


@dp.message_handler(lambda message: message.chat.type == 'private')
async def echo(message: types.Message):
    await message.forward(
        chat_id=config['chatId']
    )
    await message.reply('Forwarded!')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
