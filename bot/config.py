from urllib.parse import urljoin
import os

try:
    with open('token.txt') as f:
        BOT_API_TOKEN = f.readline().strip()
except:
    BOT_API_TOKEN = os.getenv('BOT_API_TOKEN')

with open('messages/start.txt') as f:
    START_MESSAGE = f.read()

with open('messages/help.txt') as f:
    HELP_MESSAGE = f.read()

with open('messages/code.txt') as f:
    CODE_INFO = f.read()

PROJECT_SUBDOMAIN = os.getenv('PROJECT_SUBDOMAIN')

WEBAPP_HOST = f'https://{PROJECT_SUBDOMAIN}.herokuapp.com/'
WEBHOOK_PATH = '/webhook/' + BOT_API_TOKEN[::-1]

WEBHOOK_URL = urljoin(WEBAPP_HOST, WEBHOOK_PATH)

WEBAPP_PORT = os.getenv('PORT')
