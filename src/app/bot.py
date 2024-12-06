import logging
from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage

from src.app.routers.start import start_router
from src.app.routers.auth import auth_router
from src.app.routers.order_status import status_router
from src.config import config


bot: Bot = Bot(
    token=config.telegram.token,
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


async def run_aiogram_bot() -> None:
    logging.basicConfig(level=logging.INFO)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
