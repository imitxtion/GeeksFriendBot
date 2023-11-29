import text
import requests
import asyncio

from keyboards import inline
from aiogram import Router, F
from aiogram.types import CallbackQuery, Message, URLInputFile
from aiogram.filters import Filter

router = Router()

@router.callback_query(F.data=='tiktok')
async def cb_tiktok(cb: CallbackQuery):
    await cb.message.answer(text.tiktok_assistant_menu, reply_markup=inline.tiktok_assistant_kb)

@router.callback_query(F.data=='download_video')
async def cb_download_video(cb: CallbackQuery):
    await cb.message.answer(text.tt_video_download)

    @router.message(LinkFilter())
    async def link_handler(message: Message):
        link = message.text
        msg = await message.answer('⏳ Processing...')

        url = "https://tiktok-video-no-watermark2.p.rapidapi.com/"
        querystring = {"url":link, "hd":"1"}
        headers = {
            "X-RapidAPI-Key": "d1cc32fd41msh014d95d4d984dbcp1d37a1jsnfd96bc01fb8d",
            "X-RapidAPI-Host": "tiktok-video-no-watermark2.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)

        try:
            video_link = response.json()['data']['play']
        except KeyError:
            await msg.edit_text('❌ Link that you\'ve sent is incorrect. Try another one.')

        await msg.edit_text('Sending the video... \n<u>It\'ll take a while if the video is high quality.</u>')
        await message.answer_video(URLInputFile(video_link))
        await msg.delete()

@router.callback_query(F.data=='generate_tags')
async def cb_generate_tags(cb: CallbackQuery):
    await cb.message.answer(text.tiktok_assistant_menu, reply_markup=inline.tiktok_assistant_kb)

# filter for links
class LinkFilter(Filter):
    async def __call__(self, message: Message) -> bool:
        return message.text.startswith('http')