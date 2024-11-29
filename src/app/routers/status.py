from aiogram import F, Router
from aiogram.types import Message
from typing import Any, Dict

from src.app.keyboards.status import order_status_kb
from src.database.services.service import user_service
from src.formatter.message import get_message
from src.service import api
from src.utils import load_json
from src.config import config


status_router = Router()


@status_router.message(F.text == "Статус заказа")
async def get_order_status(message: Message) -> None:
    user_id: int = message.from_user.id
    user = await user_service.get_user(user_id=user_id)
    phone: str = user.phone
    orders: Dict[str, Any] = await api.get_user_orders(phone=phone)
    if len(orders['data']['orders']) != 0:
        for order in orders['data']['orders']:
            text: str = await get_message(order=order)
            await message.answer(
                text=text,
                reply_markup=await order_status_kb()
            )
    else:
        text: Dict[str, str] = await load_json(path=config.messages.auth)
        await message.answer(
            text=text['empty'],
            reply_markup=...
        )
        await message.answer(text=text['later'])
