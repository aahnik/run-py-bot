import os
from secrets import token_urlsafe

with open('messages/start.txt') as f:
    START_MESSAGE = f.read()

with open('messages/help.txt') as f:
    HELP_MESSAGE = f.read()

with open('messages/code.txt') as f:
    CODE_INFO = f.read()


API_TOKEN = os.getenv('API_TOKEN')
assert API_TOKEN

HEROKU_APP_NAME = os.getenv('HEROKU_APP_NAME')
assert HEROKU_APP_NAME

webhook_secret = token_urlsafe(32)

# webhook settings
WEBHOOK_HOST = f'https://{HEROKU_APP_NAME}.herokuapp.com'
WEBHOOK_PATH = f'/webhook/{webhook_secret}'
WEBHOOK_URL = f'{WEBHOOK_HOST}{WEBHOOK_PATH}'

# webserver settings
WEBAPP_HOST = '0.0.0.0'
WEBAPP_PORT = int(os.getenv('PORT'))
