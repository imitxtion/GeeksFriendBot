from aiogram import F, Router
from aiogram.types import Message

router = Router()

@router.message()
async def react_wrong_msg(msg: Message):
    await msg.reply('❌ Sorry, I don\'t understand you. Use "/commands" to see the list of available commands.')