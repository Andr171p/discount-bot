from aiogram.types import ReplyKeyboardMarkup
from aiogram.types import KeyboardButton
from aiogram.types import InlineKeyboardButton
from aiogram.types import InlineKeyboardMarkup
from typing import List


async def order_status_kb() -> ReplyKeyboardMarkup:
    keyboard_list: List[List[KeyboardButton]] = [
        [KeyboardButton(text="Статус заказа")]
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=keyboard_list,
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Узнать статус заказа"
    )
    return keyboard


async def pay_link_kb(url: str) -> InlineKeyboardMarkup:
    keyboard_list: List[List[InlineKeyboardButton]] = [
        [InlineKeyboardButton(text="Оплатить", url=url)]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=keyboard_list)
    return keyboard
