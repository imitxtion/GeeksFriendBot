import asyncio, logging

from aiogram import Bot, Dispatcher
from motor.motor_asyncio import AsyncIOMotorClient
from handlers import commands, user_message, callbacks, state_handlers
from utils.start_stop import bot_start, bot_stop
from utils import secret_values

async def main():
    bot = Bot(token=secret_values.TOKEN, parse_mode='HTML')
    dp = Dispatcher()
    cluster =  AsyncIOMotorClient(secret_values.DB_CONNECTION)
    db = cluster.GeeksFriendBot

    dp.include_routers(
        commands.router,
        callbacks.router,
        state_handlers.router,
        user_message.router
    )
    dp.startup.register(bot_start)
    dp.shutdown.register(bot_stop)

    logging.basicConfig(level=logging.INFO)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, db=db)

if __name__ == '__main__':
    asyncio.run(main())