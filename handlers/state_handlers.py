import requests
import openai

from aiogram import Router, Bot, Dispatcher
from aiogram.types import Message, URLInputFile
from utils import text
from utils.config_reader import config
from utils.states import PickState

router = Router()
dp = Dispatcher()

@router.message(PickState.tt_downloading)
async def download_video(msg: Message):
    if ('http' not in msg.text 
        or 'tiktok' not in msg.text
        or 'video' not in msg.text):
        await msg.answer(text.tt_wrong_format)
    else:
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

@router.message(PickState.talking_chatgpt)
async def start_chatgpt(msg: Message):
    openai.api_key = config.openai_api_key.get_secret_value()
    response = openai.completions.create(
        model='gpt-3.5-turbo-1106',
        prompt=f'User: {msg.text}\nAssistant:'
    )
    await msg.answer(response.choices[0].text.strip())

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