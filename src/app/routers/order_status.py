from aiogram import F, Router
from aiogram.types import Message
from typing import Any, Dict, List


from src.app.schemas.order import OrderSchema
from src.message.order_status import OrderStatus
from src.database.services.service import user_service
from src.orders_api import service as api
from src.utils import load_json
from src.config import settings


status_router = Router()


@status_router.message(F.text == "Статус заказа")
async def get_order_status(message: Message) -> None:
    user_id: int = message.from_user.id
    user = await user_service.get_user(user_id)
    phone: str = user.phone
    response: Dict[str, Any] = await api.get_user_orders(phone=phone)
    orders: List[Dict[str, Any]] = response['data']['orders']
    if len(orders) != 0:
        for order in orders:
            if order['project'] == "Дисконт Суши":
                order_status = OrderStatus(order=OrderSchema(**order))
                bot_message = await order_status.get_bot_message(user_id=user_id)
                await message.answer(
                    text=bot_message.text,
                    reply_markup=bot_message.keyboard
                )
    else:
        template: Dict[str, str] = await load_json(path=settings.messages.auth)
        await message.answer(
            text=template['empty']
        )
