from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from src.config import settings
from src.utils import load_json
from src.app.keyboards.start import start_kb
from src.app.keyboards.order_status import order_status_kb
from src.database.services.service import user_service


start_router = Router()


@start_router.message(Command("start"))
async def start(message: Message) -> None:
    user_id: int = message.from_user.id
    username: str = message.from_user.username
    if await user_service.get_user(user_id) is not None:
        text = await load_json(path=settings.msg.start)
        await message.answer(
            text=text['already_auth'],
            reply_markup=await order_status_kb()
        )
    else:
        text = await load_json(path=settings.msg.start)
        await message.answer(
            text=text['start'].format(username=username),
            reply_markup=await start_kb()
        )
