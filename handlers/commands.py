from aiogram import Router
from aiogram.filters.command import Command, CommandStart
from aiogram.types import Message
from aiogram.fsm.context import FSMContext 
from keyboards import inline
from utils import text
from utils.states import PickState

router = Router()

@router.message(CommandStart())
async def cmd_start(msg: Message, state: FSMContext):
    await state.set_state(PickState.info_viewing)
    await msg.answer(text.greeting.format(name=msg.from_user.full_name.title()), reply_markup=inline.main_kb)

@router.message(Command('info'))
async def cmd_start(msg: Message, state: FSMContext):
    await state.set_state(PickState.info_viewing)
    await msg.answer(text.info)

@router.message(Command('menu'))
async def cmd_menu(msg: Message, state: FSMContext):
    await state.set_state(PickState.menu_viewing)
    await msg.answer(text.menu, reply_markup=inline.main_kb)

@router.message(Command('commands'))
async def cmd_commands(msg: Message, state: FSMContext):
    await state.set_state(PickState.commands_viewing)
    await msg.answer(text.see_commands)

@router.message(Command('video'))
async def cmd_video(msg: Message, state: FSMContext):
    await state.set_state(PickState.tt_downloading)
    await msg.answer(text.tt_video_download)

@router.message(Command('tags'))
async def cmd_feedback(msg: Message, state: FSMContext):
    await state.set_state(PickState.function_unavailable)     # tt_generating_tags
    await msg.answer(text.function_unavailable)     # tt_generate_tags

@router.message(Command('chatgpt'))
async def cmd_commands(msg: Message, state: FSMContext):
    await state.set_state(PickState.function_unavailable)    # talking_chatgpt
    await msg.answer(text.function_unavailable)     # talk_chatgpt

@router.message(Command('todo'))
async def cmd_commands(msg: Message, state: FSMContext):
    await state.set_state(PickState.todo_writing)
    await msg.answer()

@router.message(Command('ongoings'))
async def cmd_commands(msg: Message, state: FSMContext):
    await state.set_state(PickState.browse_ongoings)
    await msg.answer()

@router.message(Command('favanime'))
async def cmd_commands(msg: Message, state: FSMContext):
    await state.set_state(PickState.edit_anime_list)
    await msg.answer()

@router.message(Command('feedback'))
async def cmd_feedback(msg: Message, state: FSMContext):
    await state.set_state(PickState.sending_feedback)
    await msg.answer(text.send_feedback)

@router.message(Command('coffee'))
async def cmd_feedback(msg: Message, state: FSMContext):
    await state.set_state(PickState.buying_coffee)
    await msg.answer(text.buy_coffee)