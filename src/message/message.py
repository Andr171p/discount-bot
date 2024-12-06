from dataclasses import dataclass
from aiogram.types import InlineKeyboardMarkup


@dataclass
class BotMessage:
    user_id: int
    text: str
    keyboard: InlineKeyboardMarkup | None
