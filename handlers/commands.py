import text

from aiogram import Router
from aiogram.filters.command import Command, CommandStart
from aiogram.types import Message
from keyboards import inline

router = Router()

@router.message(CommandStart())
async def cmd_start(msg: Message):
    await msg.answer(text.greeting.format(name=msg.from_user.full_name.title()), reply_markup=inline.main_kb)

@router.message(Command('menu'))
async def cmd_menu(msg: Message):
    await msg.answer(text.menu, reply_markup=inline.main_kb)