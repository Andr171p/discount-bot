from aiogram import F, Router
from aiogram.types import Message

from src.database.services.service import user_service


status_router = Router()


@status_router.message(F.text == "Статус заказа")
async def get_order_status(message: Message) -> None:
    user_id: int = message.from_user.id
    user = await user_service.get_user(user_id=user_id)
    # implementing receiving order status from api ...
    ...
