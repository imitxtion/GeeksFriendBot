import asyncio, logging, text

from aiogram import Bot, Dispatcher, F, Router
from aiogram.filters.command import Command, CommandStart
from aiogram.types import Message
from config_reader import config
from handlers import commands, user_message
from start_stop import bot_start, bot_stop

async def main():
    bot = Bot(token=config.token.get_secret_value(), parse_mode='HTML')
    dp = Dispatcher()

    dp.include_routers(
        commands.router,
        user_message.router
    )
    dp.startup.register(bot_start)
    dp.shutdown.register(bot_stop)

    logging.basicConfig(level=logging.INFO)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())