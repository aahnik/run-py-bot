''' Script to start the bot '''

import logging

from run_py_bot import main

logging.basicConfig(level=logging.INFO)


if __name__ == "__main__":
    bot = main.bot
    main.webhook()
