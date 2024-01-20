import asyncio

from aiogram import Router
from aiogram.filters.command import Command, CommandStart
from aiogram.types import Message
from aiogram.fsm.context import FSMContext 
from pymongo.errors import DuplicateKeyError
from motor.core import AgnosticDatabase as MDB
from contextlib import suppress
from datetime import datetime
from keyboards import inline
from utils import text
from utils.states import PickState

router = Router()

@router.message(CommandStart())
async def cmd_start(msg: Message, state: FSMContext, db: MDB):
    await state.set_state(PickState.info_viewing)
    await msg.answer(text.greeting.format(name=msg.from_user.full_name.title()), reply_markup=inline.main_kb)
    with suppress(DuplicateKeyError):
        await db.Bot_users.insert_one(
            {
                '_id' : msg.from_user.id,
                'username' : f'@{msg.from_user.username}',
                'launch_date' : datetime.now().strftime("%Y-%m-%d, %H:%M:%S"),
            }
        )

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
    await state.set_state(PickState.talking_chatgpt)
    await msg.answer(text.talk_chatgpt)

@router.message(Command('todo'))
async def cmd_todo(msg: Message, state: FSMContext):
    await state.set_state(PickState.checking_todo_menu)
    await msg.answer(text.todo_info, reply_markup=inline.todo_kb)

@router.message(Command('newtask'))
async def add_task(msg: Message, state: FSMContext):
    await state.set_state(PickState.adding_new_task)
    try:
        user_tasks = {}
        task_info = msg.text.replace("/newtask", "").strip()
        task_data = task_info.split('#')

        if len(task_data) >= 2:
            task_description = task_data[0].strip()
            task_datetime_str = task_data[1].strip()

            task_datetime = datetime.strptime(task_datetime_str, "%Y-%m-%d %H:%M")

            task = {
                'description': task_description,
                'datetime': task_datetime,
                'user_id': msg.from_user.id
            }
            
            user_id = msg.from_user.id
            if user_id not in user_tasks:
                user_tasks[user_id] = []
            user_tasks[user_id].append(task)
            
            await msg.reply(text.adding_task_success.format(task=task_description, time= task_datetime))
            time_difference = task_datetime - datetime.now()

            await asyncio.sleep(time_difference.total_seconds())
            await msg.reply(text.task_remind.format(task= task_description, time= task_datetime))

        else:
            await msg.reply(text.adding_task_error)
            
    except Exception:
        await msg.reply(text.adding_task_error)

@router.message(Command('animenews'))
async def cmd_browse_news(msg: Message, state: FSMContext):
    await state.set_state(PickState.browsing_news)
    await msg.answer('+')

@router.message(Command('sauce'))
async def cmd_find_sauce(msg: Message, state: FSMContext):
    await state.set_state(PickState.looking_for_sauce)
    await msg.answer(text.find_sauce)

@router.message(Command('favanime'))
async def cmd_fav_anime_list(msg: Message, state: FSMContext):
    await state.set_state(PickState.edit_anime_list)
    await msg.answer('+')

@router.message(Command('feedback'))
async def cmd_feedback(msg: Message, state: FSMContext):
    await state.set_state(PickState.sending_feedback)
    await msg.answer(text.send_feedback)

@router.message(Command('coffee'))
async def cmd_feedback(msg: Message, state: FSMContext):
    await state.set_state(PickState.buying_coffee)
    await msg.answer(text.buy_coffee)