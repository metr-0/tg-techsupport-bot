import logging
import json

from aiogram import Bot, Dispatcher

logging.basicConfig(level=logging.INFO)

with open('config.json') as config_file:
    config = json.load(config_file)

bot = Bot(token=config['token'])
dp = Dispatcher(bot)
