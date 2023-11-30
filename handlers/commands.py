import text

from aiogram import Router
from aiogram.filters.command import Command, CommandStart
from aiogram.types import Message
from keyboards import inline
from aiogram.fsm.context import FSMContext 
from utils.states import PickState

router = Router()

@router.message(CommandStart())
async def cmd_start(msg: Message, state: FSMContext):
    await state.set_state(PickState.info_viewing)
    await msg.answer(text.greeting.format(name=msg.from_user.full_name.title()), reply_markup=inline.main_kb)

@router.message(Command('menu'))
async def cmd_menu(msg: Message, state: FSMContext):
    await state.set_state(PickState.menu_viewing)
    await msg.answer(text.menu, reply_markup=inline.main_kb)