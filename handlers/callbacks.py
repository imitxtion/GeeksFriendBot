import requests

from keyboards import inline
from aiogram import Router, F, Bot, Dispatcher
from aiogram.types import CallbackQuery, Message, URLInputFile
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

@router.message(PickState.tt_downloading)
async def download_video(msg: Message):
    if ('http' not in msg.text 
        or 'tiktok' not in msg.text
        or 'video' not in msg.text):
        await msg.answer(text.tt_wrong_format)
    else:
        #@router.message(LinkFilter())
        #async def link_handler(message: Message):
        link = msg.text
        mssg = await msg.answer('⏳ Processing...')

        url = "https://tiktok-video-no-watermark2.p.rapidapi.com/"
        querystring = {"url":link, "hd":"1"}
        headers = {
            "X-RapidAPI-Key": config.rapidapi_key.get_secret_value(),
            "X-RapidAPI-Host": "tiktok-video-no-watermark2.p.rapidapi.com"
        }
        response = requests.get(url, headers=headers, params=querystring)
        video_link = response.json()['data']['play']

        await mssg.edit_text(text.tt_sending_video)
        await msg.answer_video(URLInputFile(video_link))
        await mssg.delete()

@router.callback_query(F.data=='generate_tags')
async def cb_generate_tags(cb: CallbackQuery, state: FSMContext):
    await cb.answer()
    await state.set_state(PickState.tt_generating_tags)
    await cb.message.answer(text.tt_assistant_menu, reply_markup=inline.tiktok_assistant_kb)

@router.callback_query(F.data=='feedback')
async def cb_send_feedback(cb: CallbackQuery, state: FSMContext):
    await cb.answer()
    await state.set_state(PickState.sending_feedback)
    await cb.message.answer(text.send_feedback)

@router.message(PickState.sending_feedback)
async def send_feedback_to_admin(msg: Message, bot: Bot):
    username = msg.from_user.username
    user_id = msg.from_user.id
    user_feedback = msg.text
    admin_message = text.admin_new_message.format(
        username=username, 
        user_id=user_id, 
        user_feedback=user_feedback
    )

    try:
        await bot.send_message(config.admin_id.get_secret_value(), admin_message)
        await msg.answer(text.send_feedback_success)
    except:
        await msg.answer(text.send_feedback_error)