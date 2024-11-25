from aiogram import F, Router
from aiogram.types import Message

from src.database.services.service import user_service
from src.api.service import OrderServiceAPI


status_router = Router()

order_service = OrderServiceAPI()


@status_router.message(F.text == "Статус заказа")
async def get_order_status(message: Message) -> None:
    user_id: int = message.from_user.id
    user = await user_service.get_user(user_id=user_id)
    order = await order_service.get_order(phone=user.phone)
    ...
    await message.answer(
        text=...,
        reply_markup=...
    )
