from aiogram.dispatcher.filters.state import StatesGroup, State


class search(StatesGroup):
    user_id = State()


class deposit(StatesGroup):
    sum = State()


class deal(StatesGroup):
    sum = State()
