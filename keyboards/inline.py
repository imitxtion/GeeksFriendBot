from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

main_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='🚀 TikTok Assistant', callback_data='tiktok'),
            InlineKeyboardButton(text='💬 ChatGPT', callback_data='chatgpt')        
        ],
        [
            InlineKeyboardButton(text='📝 To-Do List', callback_data='todo'),
            InlineKeyboardButton(text='⛩ Anime Assistant', callback_data='anime')
        ],
        [
            InlineKeyboardButton(text='📬 Send Feedback', callback_data='feedback'),
        ],
        [
            InlineKeyboardButton(text='☕ Support the Bot', callback_data='buy_coffee')
        ]
    ]
)

tiktok_assistant_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Video Downloader 🎥', callback_data='download_video'),
            InlineKeyboardButton(text='Tags Generator 🏷️', callback_data='generate_tags')
        ]
    ]
)

todo_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Add task ➕', callback_data='add_task'),
            InlineKeyboardButton(text='My tasks 📃', callback_data='my_tasks')
        ]
    ]
)

anime_assistant_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='News ⛩', callback_data='anime_news'),
            InlineKeyboardButton(text='Name finder 🔎', callback_data='sauce')
        ]
    ]
)