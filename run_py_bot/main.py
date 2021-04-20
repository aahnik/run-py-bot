''' This module uses aiogram to make the telegram bot.
The various commands and messages sent to the bot are handled by this script
'''

import logging

from aiogram import (Bot, Dispatcher, executor, types)
from aiogram.types import (InlineQuery, InlineQueryResultArticle,
                           InputTextMessageContent)
from aiogram.utils.executor import start_webhook
from aiogram.contrib.middlewares.logging import LoggingMiddleware

from .rextester import run_python_rextester
from .helpers import parse_response, results
from .config import API_TOKEN, START_MESSAGE, HELP_MESSAGE, CODE_INFO


bot = Bot(token=API_TOKEN)

dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    ''' This handles the start command. '''

    await message.reply(START_MESSAGE, parse_mode='Markdown')


@dp.message_handler(commands=['help'])
async def bot_help(message: types.Message):
    ''' This handles the help command. '''

    await message.reply(HELP_MESSAGE, parse_mode='Markdown')


@dp.message_handler(commands=['code'])
async def code(message: types.Message):
    ''' This handles the code command. '''

    await message.reply(CODE_INFO, parse_mode='Markdown')


@dp.message_handler(commands=['e'])
async def deprecated(message: types.Message):
    ''' This handles the e command which has been deprecated. '''

    await message.reply('''Usage of /e has been deprecated.
                \nAny one-line message is by default passed to the eval function.''')


@dp.message_handler(text=['hi', 'hello', 'Hi', 'Hello'])
async def sweet(message: types.Message):
    ''' When the user says hi or hello, the bot gives a sweet reply. '''

    user = message.from_user.full_name
    await message.reply(f'Hi {user} 🥰')


@dp.message_handler()
async def run_code(message: types.Message):
    ''' Any normal text message except those handled by the above handlers, is executed as code .'''

    if not message.text.startswith('/'):
        inform = await message.reply('I recieved your code ...')

        resp = await run_python_rextester(message.text.strip('\n'))
        output = parse_response(resp)

        if output:
            output_message = await message.reply(output['message'])
            await output_message.reply(output['stats'])
        else:
            await message.reply('Some error occured while parsing output')
        await inform.delete()

    else:
        await message.reply('I could not understand that command. 😢')


@dp.inline_handler()
async def inline_echo(inline_query: InlineQuery):
    ''' Calling the bot inline gives the user some sharable links. '''

    text = inline_query.query or 'default'
    items = [InlineQueryResultArticle(
        id=result_id,
        title=title,
        input_message_content=InputTextMessageContent(content))
        for result_id, title, content in results(text)]
    if __name__ == '__main__':
        cache_time = 1
    else:
        cache_time = 300
    await bot.answer_inline_query(inline_query.id, results=items, cache_time=cache_time)


async def on_startup(dp: Dispatcher):
    ''' Code to run when webhook starts.

    Args:
        dp (Dispatcher): dispatcher object
    '''
    from run_py_bot.config import WEBHOOK_URL

    await bot.set_webhook(WEBHOOK_URL,drop_pending_updates=True) # drop pending to prevent bot from responding twice to a message after waking
    logging.warning('Starting connection')


async def on_shutdown(dp: Dispatcher):
    ''' Code to run when webhook is shutdown.

    Args:
        dp (Dispatcher): [description]
    '''

    logging.warning('Ending connection')


async def info():
    return bot.get_webhook_info()


def poll():
    ''' The bot is started by the main method. '''

    executor.start_polling(dp, skip_updates=True)


def webhook():
    ''' Webhook connection. '''
    from run_py_bot.config import WEBHOOK_PATH,WEBAPP_PORT,WEBAPP_HOST
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
    )
