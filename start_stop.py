from aiogram import Bot
from mine.params import my_id

async def bot_start(bot: Bot):
    await bot.send_message(my_id, text='✅ <b>Bot launched!</b>')

async def bot_stop(bot: Bot):
    await bot.send_message(my_id, text='❌ <b>Bot stopped!</b>')