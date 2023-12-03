from utils import text, secret_values
from aiogram import Bot

async def bot_start(bot: Bot):
    await bot.send_message(secret_values.ADMIN_ID, text= text.bot_start)

async def bot_stop(bot: Bot):
    await bot.send_message(secret_values.ADMIN_ID, text= text.bot_stop)