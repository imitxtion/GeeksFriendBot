import text

from aiogram import Router
from aiogram.types import Message

router = Router()

@router.message()
async def react_wrong_msg(msg: Message):
    await msg.reply(text.wrong_message)