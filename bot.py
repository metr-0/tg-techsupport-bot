import logging
import json

from aiogram import Bot, Dispatcher

logging.basicConfig(level=logging.INFO)

with open('config/config.json', 'r', encoding='utf-8') as config_file:
    config = json.load(config_file)

with open('config/templates.json', 'r', encoding='utf-8') as templates_file:
    templates = json.load(templates_file)

bot = Bot(token=config['token'])
dp = Dispatcher()

bot_id = bot.id


async def main() -> None:
    await dp.start_polling(bot)
