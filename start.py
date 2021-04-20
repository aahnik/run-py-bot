''' Script to start the bot '''

import logging

from run_py_bot import main

from run_py_bot.config import HEROKU_APP_NAME

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    if HEROKU_APP_NAME:
        main.webhook()
    else:
        main.poll()
