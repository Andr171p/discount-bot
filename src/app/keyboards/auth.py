from aiogram.types import InlineKeyboardMarkup
from aiogram.types import InlineKeyboardButton
from typing import List


async def valid_phone_kb() -> InlineKeyboardMarkup:
    keyboard_list: List[List[InlineKeyboardButton]] = [
        [InlineKeyboardButton(text="да", callback_data="valid_phone")],
        [InlineKeyboardButton(text="нет", callback_data="invalid_phone")]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=keyboard_list)
    return keyboard
