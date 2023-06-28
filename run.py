from aiogram import executor
from bot import *

from handlers.signup import *
from handlers.test import *
from handlers.answer import *
from handlers.question import *

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
