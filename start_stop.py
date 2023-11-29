from aiogram import Bot
from mine.params import my_id
from config_reader import config

async def bot_start(bot: Bot):
    await bot.send_message(config.admin_id.get_secret_value(), text='✅ <b>Bot launched!</b>')

async def bot_stop(bot: Bot):
    await bot.send_message(config.admin_id.get_secret_value(), text='❌ <b>Bot stopped!</b>')