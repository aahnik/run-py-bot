import asyncio
from run_py_bot import config
from aiogram import Bot

bot = Bot(token=config.API_TOKEN)


async def hook_and_crook():
    await bot.delete_webhook()
    await bot.set_webhook(config.WEBHOOK_URL)
    print(await bot.get_webhook_info())

asyncio.run(hook_and_crook())
