import text
import requests
import asyncio

from keyboards import inline
from aiogram import Router, F
from aiogram.types import CallbackQuery, Message, URLInputFile
from aiogram.filters import Filter
from config_reader import config

router = Router()

@router.callback_query(F.data=='tiktok')
async def cb_tiktok(cb: CallbackQuery):
    await cb.message.answer(text.tt_assistant_menu, reply_markup=inline.tiktok_assistant_kb)

@router.callback_query(F.data=='download_video')
async def cb_download_video(cb: CallbackQuery):
    await cb.message.answer(text.tt_video_download)

    @router.message()
    async def wrong_format_alert(msg: Message):
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
async def cb_generate_tags(cb: CallbackQuery):
    await cb.message.answer(text.tt_assistant_menu, reply_markup=inline.tiktok_assistant_kb)

# # filter for links
# class LinkFilter(Filter):
#     async def __call__(self, message: Message) -> bool:
#         return message.text.startswith('http')