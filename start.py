''' Script to start the bot '''

import logging

from bot import bot

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    bot.webhook()
