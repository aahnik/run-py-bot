from urllib.parse import urljoin
import os

try:
    with open('token.txt') as f:
        BOT_API_TOKEN = f.readline().strip()
except:
    BOT_API_TOKEN = os.getenv('BOT_API_TOKEN')

assert BOT_API_TOKEN

with open('messages/start.txt') as f:
    START_MESSAGE = f.read()

with open('messages/help.txt') as f:
    HELP_MESSAGE = f.read()

with open('messages/code.txt') as f:
    CODE_INFO = f.read()

PROJECT_SUBDOMAIN = os.getenv('APP_NAME')
DOMAIN = os.getenv('DOMAIN')

# webhook settings
WEBHOOK_HOST = f'https://{PROJECT_SUBDOMAIN}.{DOMAIN}.com'
WEBHOOK_PATH = '/webhook/' + BOT_API_TOKEN[::-1]
WEBHOOK_URL = urljoin(WEBHOOK_HOST, WEBHOOK_PATH)


# webapp settings
WEBAPP_HOST = 'localhost'
WEBAPP_PORT = os.getenv('PORT')

# way to run
METHOD = os.getenv('METHOD', 'polling')
# METHOD can be `polling` or `webhook`
