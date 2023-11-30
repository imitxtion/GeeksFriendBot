import text

from aiogram import Bot
from config_reader import config

async def bot_start(bot: Bot):
    await bot.send_message(config.admin_id.get_secret_value(), text= text.bot_start)

async def bot_stop(bot: Bot):
    await bot.send_message(config.admin_id.get_secret_value(), text= text.bot_stop)