import requests

from keyboards import inline
from aiogram import Router, F, Bot, Dispatcher
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from utils import text
from utils.config_reader import config
from utils.states import PickState

router = Router()
dp = Dispatcher()
bot = Bot(token=config.token.get_secret_value(), parse_mode='HTML')

@router.callback_query(F.data=='tiktok')
async def cb_tiktok(cb: CallbackQuery, state: FSMContext):
    await cb.answer()
    await state.set_state(PickState.tt_assistant)
    await cb.message.answer(text.tt_assistant_menu, reply_markup=inline.tiktok_assistant_kb)

@router.callback_query(F.data=='download_video')
async def cb_download_video(cb: CallbackQuery, state: FSMContext):
    await cb.answer()
    await state.set_state(PickState.tt_downloading)
    await cb.message.answer(text.tt_video_download)

@router.callback_query(F.data=='generate_tags')
async def cb_generate_tags(cb: CallbackQuery, state: FSMContext):
    await cb.answer()
    await state.set_state(PickState.tt_generating_tags)
    await cb.message.answer(text.tt_generate_tags)

@router.callback_query(F.data=='feedback')
async def cb_send_feedback(cb: CallbackQuery, state: FSMContext):
    await cb.answer()
    await state.set_state(PickState.sending_feedback)
    await cb.message.answer(text.send_feedback)