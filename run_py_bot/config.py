import os
from dotenv import load_dotenv

load_dotenv('.env')

with open('messages/start.txt') as f:
    START_MESSAGE = f.read()

with open('messages/help.txt') as f:
    HELP_MESSAGE = f.read()

with open('messages/code.txt') as f:
    CODE_INFO = f.read()


API_TOKEN = os.getenv('API_TOKEN')
assert API_TOKEN

HEROKU_APP_NAME = os.getenv('HEROKU_APP_NAME')

if HEROKU_APP_NAME:

    # webhook settings
    WEBHOOK_HOST = f'https://{HEROKU_APP_NAME}.herokuapp.com'
    WEBHOOK_PATH = f'/webhook/{API_TOKEN}'
    WEBHOOK_URL = f'{WEBHOOK_HOST}{WEBHOOK_PATH}'

    # webserver settings
    WEBAPP_HOST = '0.0.0.0'
    WEBAPP_PORT = int(os.getenv('PORT'))
