from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from src.config import config


bot: Bot = Bot(
    token=config.telegram.token,
    parse_mode=ParseMode.HTML
)
dp: Dispatcher = Dispatcher(
    storage=MemoryStorage()
)