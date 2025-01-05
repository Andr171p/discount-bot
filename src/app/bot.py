from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage

from src.app.routers.start import start_router
from src.app.routers.auth import auth_router
from src.app.routers.order_status import status_router
from src.config import settings


bot: Bot = Bot(
    token=settings.bot.token,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)
dp: Dispatcher = Dispatcher(
    storage=MemoryStorage()
)

dp.include_routers(
    start_router,
    auth_router,
    status_router
)
