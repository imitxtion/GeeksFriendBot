from aiogram.fsm.state import StatesGroup, State

class PickState(StatesGroup):
    info_viewing = State()
    menu_viewing = State()
    commands_viewing = State()
    tt_assistant = State()
    tt_downloading = State()
    tt_generating_tags = State()
    talking_chatgpt = State()
    todo_writing = State()
    browse_ongoings = State()
    edit_anime_list = State()
    sending_feedback = State()
    buying_coffee = State()