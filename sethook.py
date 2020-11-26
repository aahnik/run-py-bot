from run_py_bot import config
from aiogram import Bot

bot = Bot(token=config.API_TOKEN)

bot.delete_webhook()
bot.set_webhook(config.WEBHOOK_URL)

print(bot.get_webhook_info())
