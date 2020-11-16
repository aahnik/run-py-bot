from aiogram import Bot, Dispatcher, executor, types
from .rextester import run_python_rextester
from .checks import check_long_message

with open('token.txt') as f:
    API_TOKEN = f.readline()

with open('docs/start.txt') as f:
    START_MESSAGE = f.read()

with open('docs/help.txt') as f:
    HELP_MESSAGE = f.read()

with open('docs/code.txt') as f:
    CODE_INFO = f.read()


bot = Bot(token=API_TOKEN)

dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply(START_MESSAGE, parse_mode='Markdown')


@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    await message.reply(HELP_MESSAGE, parse_mode='Markdown')


@dp.message_handler(commands=['code'])
async def help(message: types.Message):
    await message.reply(CODE_INFO, parse_mode='Markdown')


@dp.message_handler(commands=['/e'])
async def e(message: types.Message):
    await message.reply('''Usage of /e has been deprecated since v0.1.0
                \nAny one-line message is by default passed to the eval function''')


@dp.message_handler()
async def run_code(message: types.Message):
    if message.text:
        await message.reply('I recieved your code')

        text = message.text.strip('\n')

        if '\n' not in text:
            text = f'print(eval("{text}"))'

        resp = await run_python_rextester(text)

        if resp['Errors'] == 'Too many requests...':
            message.reply('Try after some time')

        output = f'''{resp['Result'] if resp['Result'] else 'No result' }
                    \n{resp['Errors']}
                    \n{resp['Warnings']}'''

        reply_message = check_long_message(output)

        keyboard_markup = types.InlineKeyboardMarkup(row_width=3)

        row_btns = types.InlineKeyboardButton(
            'See Stats', callback_data='stats')

        keyboard_markup.row(row_btns)

        await message.reply(reply_message, reply_markup=keyboard_markup)

    else:
        await message.reply('Your message has no text')


def main():
    executor.start_polling(dp, skip_updates=True)


if __name__ == '__main__':
    main()
