from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


def start_kb() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    builder.button(text="Зарегистрироваться", request_contact=True)
    return builder.as_markup(
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Нажмите для мгновенной регистрации"
    )


def payment_kb(pay_link: str) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    if pay_link:
        builder.button(text="Оплатить", url=pay_link)
    else:
        builder.button(text="Не оплачен", callback_data="payment_required")
    return builder.as_markup()


def confirmed_payment_kb(pay_link: str) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    if pay_link:
        builder.button(text="ОПЛАЧЕН", url=pay_link)
    else:
        builder.button(text="ОПЛАЧЕН", callback_data="confirmed")
    return builder.as_markup()
