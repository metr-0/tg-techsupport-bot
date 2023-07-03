from aiogram.filters import Command

from bot import dp, config, templates

from aiogram import types, F, Bot


@dp.message(Command('ping'))
async def ping(message: types.Message) -> None:
    await message.reply('pong')


@dp.message(Command('id'))
async def get_id(message: types.Message) -> None:
    await message.reply(f'Chat ID: {message.chat.id}')


@dp.message(F.chat.type == 'private' and Command('start', 'help'))
async def help_msg(message: types.Message) -> None:
    await message.reply(templates['helpMessage'])


@dp.message(
    F.chat.id == config['chatId'] and F.reply_to_message.forward_from
)
async def answer(message: types.Message, bot: Bot) -> None:
    user_id = message.reply_to_message.forward_from.id

    await bot.send_message(
        chat_id=user_id,
        text=templates['answerReceived']
    )
    await message.forward(chat_id=user_id)
    await message.reply(templates['answerSent'])


@dp.message(F.chat.type == 'private')
async def question(message: types.Message) -> None:
    await message.forward(chat_id=config['chatId'])
    await message.reply(templates['questionSent'])
