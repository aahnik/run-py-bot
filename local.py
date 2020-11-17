import logging
from bot import bot

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO, datefmt='%d/%m/%Y %I:%M:%S %p')

logger = logging.getLogger()
logger.setLevel(logging.INFO)

bot.poll()
