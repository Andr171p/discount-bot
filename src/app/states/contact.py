from aiogram.filters.state import State, StatesGroup


class ContactForm(StatesGroup):
    user_id = State()
    username = State()
    phone = State()
