''' This module uses aiogram to make the telegram bot. 
The various commands and messages sent to the bot are handled by this script
'''

import logging

from aiogram import (Bot, Dispatcher, executor, types)
from aiogram.types import (InlineQuery,
                           InputTextMessageContent,
                           InlineQueryResultArticle)

from .rextester import run_python_rextester
from .helpers import parse_response, results

with open('token.txt') as f:
    API_TOKEN = f.readline()

with open('messages/start.txt') as f:
    START_MESSAGE = f.read()

with open('messages/help.txt') as f:
    HELP_MESSAGE = f.read()

with open('messages/code.txt') as f:
    CODE_INFO = f.read()


bot = Bot(token=API_TOKEN)

dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    ''' This handles the start command. '''

    await message.reply(START_MESSAGE, parse_mode='Markdown')


@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    ''' This handles the help command. '''

    await message.reply(HELP_MESSAGE, parse_mode='Markdown')


@dp.message_handler(commands=['code'])
async def help(message: types.Message):
    ''' This handles the code command. '''

    await message.reply(CODE_INFO, parse_mode='Markdown')


@dp.message_handler(commands=['/e'])
async def e(message: types.Message):
    ''' This handles the e command which has been deprecated. '''

    await message.reply('''Usage of /e has been deprecated since v0.1.0
                \nAny one-line message is by default passed to the eval function''')


@dp.message_handler(text=['hi', 'hello'])
async def hi(message: types.Message):
    ''' When the user says hi or hello, the bot gives a sweet reply. '''

    user = message.from_user.full_name
    await message.reply(f'Hi {user} 🥰')


@dp.message_handler()
async def run_code(message: types.Message):
    ''' Any normal text message except those handled by the above handlers, is executed as code .'''

    if message.text:
        inform = await message.reply('I recieved your code')

        resp = await run_python_rextester(message.text.strip('\n'))
        output = parse_response(resp)

        if output:
            output_message = await message.reply(output['message'])
            await output_message.reply(output['stats'])
        else:
            await message.reply('Some error occured while parsing output')
        await inform.delete()

    else:
        await message.reply('This should not happen')


@dp.inline_handler()
async def inline_echo(inline_query: InlineQuery):
    ''' Calling the bot inline gives the user some sharable links. '''

    text = inline_query.query or 'default'
    items = [InlineQueryResultArticle(
        id=result_id,
        title=title,
        input_message_content=InputTextMessageContent(content)) for result_id, title, content in results(text)]
    if __name__ == '__main__':
        ct = 1
    else:
        ct = 300
    await bot.answer_inline_query(inline_query.id, results=items, cache_time=ct)


def main():
    ''' The bot is started by the main method. '''
    
    executor.start_polling(dp, skip_updates=True)


if __name__ == '__main__':
    ''' This module will be run directly while testing the bot locally. '''

    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO, datefmt='%d/%m/%Y %I:%M:%S %p')

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    main()
