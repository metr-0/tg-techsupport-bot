from aiogram.filters import Command

from bot import dp, config

from aiogram import types, F, Bot


@dp.message(Command('ping'))
async def ping(message: types.Message) -> None:
    await message.reply('pong')


@dp.message(Command('start', 'help'))
async def help_msg(message: types.Message) -> None:
    await message.reply('*Тут будут помощь*')


@dp.message(
    F.chat.id == config['chatId'] and F.reply_to_message.forward_from
)
async def answer(message: types.Message, bot: Bot) -> None:
    user_id = message.reply_to_message.forward_from.id

    await bot.send_message(
        chat_id=user_id,
        text='Получен ответ от техподдержки:'
    )
    await message.forward(
        chat_id=user_id
    )
    await message.reply('Ваш ответ отправлен!')


@dp.message(F.chat.type == 'private')
async def question(message: types.Message) -> None:
    await message.forward(
        chat_id=config['chatId']
    )
    await message.reply('Ваше обращение отправлено в техподдержку!')
