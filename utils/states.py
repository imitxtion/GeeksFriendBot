from aiogram import Router, F
from aiogram.filters import Command, StateFilter
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext 

class PickState(StatesGroup):
    info_viewing = State()
    menu_viewing = State()
    tt_assistant = State()
    tt_downloading = State()
    tt_generating_tags = State()
    sending_feedback = State()