from aiogram.filters.state import State, StatesGroup


class ContactForm(StatesGroup):
    phone = State()
