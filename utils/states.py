from aiogram.fsm.state import StatesGroup, State

class PickState(StatesGroup):
    info_viewing = State()
    menu_viewing = State()
    tt_assistant = State()
    tt_downloading = State()
    tt_generating_tags = State()
    sending_feedback = State()
    buying_coffee = State()