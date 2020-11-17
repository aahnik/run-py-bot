''' This module will setup logging in desired timezone and start the bot. '''

import logging
from datetime import datetime
from pytz import timezone
from bot import bot
from bot.config import PROJECT_SUBDOMAIN, METHOD


TIMEZONE = 'Asia/Kolkata'

logging.Formatter.converter = lambda *args: datetime.now(
    tz=timezone(TIMEZONE)).timetuple()

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO, datefmt='%d/%m/%Y %I:%M:%S %p')

logger = logging.getLogger()
logger.setLevel(logging.INFO)

if __name__ == "__main__":
    if METHOD == 'webhook':
        assert PROJECT_SUBDOMAIN
        bot.webhook()
    elif METHOD == 'polling':
        bot.poll()
    else:
        print('This should never happen.')
