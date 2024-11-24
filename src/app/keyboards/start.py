from aiogram.types import ReplyKeyboardMarkup
from aiogram.types import KeyboardButton
from typing import List


async def start_kb() -> ReplyKeyboardMarkup:
    keyboard_list: List[List[KeyboardButton]] = [
        [KeyboardButton(text="Регистрация", request_contact=True)]
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=keyboard_list,
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Нажмите для регистрации"
    )
    return keyboard
