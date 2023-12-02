import logging
import requests
import openai

from aiogram import Router, Bot, Dispatcher
from aiogram.types import Message, URLInputFile
from aiogram.exceptions import TelegramBadRequest
from saucenaopie import SauceNao
from saucenaopie.helper import SauceIndex
from saucenaopie.exceptions import UnknownServerError
from utils import text
from utils.config_reader import config
from utils.states import PickState

router = Router()
dp = Dispatcher()

@router.message(PickState.function_unavailable)
async def fucn_off(msg: Message):
    await msg.answer(text.function_unavailable)

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

@router.message(PickState.looking_for_sauce)
async def find_sauce(msg: Message, bot: Bot):
    mssg = await msg.answer('⏳ Processing...')
    nao = SauceNao(api_key=config.saucenao_api_key.get_secret_value())
    if msg.photo:
        res = await bot.get_file(msg.photo[-1].file_id)
        photo = await bot.download_file(res.file_path)
        try:
            sauce = nao.search(photo, result_limit=5, index=SauceIndex.ANIME and SauceIndex.H_ANIME)
        except UnknownServerError:
            await mssg.delete()
            return msg.answer(text.sauce_server_error)
        del photo
        Found = True
        try:
            for result in sauce.results:
                print(result.index, result.index.id, result.similarity, result.data)
                if result.index.id == 21:
                    Found = False
                    if result.data.urls:
                        await mssg.delete()
                        await msg.answer_photo(result.data.urls[-1],
                                                caption=f'<b>Anime:</b> {result.data.title}\n'
                                                        f'<b>Similarity:</b> {result.similarity}%\n'
                                                        f'<b>Episode:</b> {result.data.episode}\n' 
                                                        f'<b>Timestamp:</b> {result.data.timestamp}')
                    else:
                        await mssg.delete()
                        await msg.answer(f'<b>Anime:</b> {result.data.title}\n'
                                         f'<b>Similarity:</b> {result.similarity}%\n'
                                         f'<b>Episode:</b> {result.data.episode}\n' 
                                         f'<b>Timestamp:</b> {result.data.timestamp}')
                    break
                elif result.index.id == 22:
                    Found = False
                    await mssg.delete()
                    await msg.answer(f'<b>Anime:</b> {result.data.title}\n'
                                     f'<b>Similarity:</b> {result.similarity}%\n'
                                     f'<b>Episode:</b> {result.data.episode}\n' 
                                     f'<b>Timestamp:</b> {result.data.timestamp}')
                    break
            if Found:
                await mssg.delete()
                await msg.answer(text.sauce_not_found)
        except Exception as ex:
            logging.error(ex)

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