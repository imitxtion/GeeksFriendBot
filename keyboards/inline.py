from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

main_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='🚀 TikTok Assistant', callback_data='tiktok'),
            InlineKeyboardButton(text='💬 ChatGPT', callback_data='ai')        
        ],
        [
            InlineKeyboardButton(text='📝 To-Do List', callback_data='todo'),
            InlineKeyboardButton(text='⛩ Anime Assistant', callback_data='anime')
        ],
        [
            InlineKeyboardButton(text='📬 Send Feedback', callback_data='feedback'),
        ],
        [
            InlineKeyboardButton(text='☕ Support the Bot', callback_data='support')
        ]
    ]
)