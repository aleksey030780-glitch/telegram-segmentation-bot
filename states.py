from aiogram.dispatcher.filters.state import State, StatesGroup

class Quiz(StatesGroup):
    industry = State()
    scale = State()
    pain = State()
    warmth = State()
    name = State()
    phone = State()
