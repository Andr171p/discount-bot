from aiogram import F, Router
from aiogram.types import Message

from src.config import settings
from src.utils import load_json, format_phone
from src.app.keyboards import order_status
from src.app.schemas.user import UserSchema
from src.app.logger import logger
from src.database.models.user import UserModel
from src.database.services.service import user_service


auth_router = Router()


@auth_router.message(F.contact)
async def register_user(message: Message) -> None:
    user_id: int = message.from_user.id
    username: str = message.from_user.username
    phone: str = message.contact.phone_number
    user = UserSchema(
        user_id=user_id,
        username=username,
        phone=format_phone(phone)
    )
    logger.info(f"user: {user} shared contact")
    _ = await user_service.add_user(user=UserModel(**user.__dict__))
    text = await load_json(path=settings.msg.auth)
    await message.answer(
        text=text['success'],
        # reply_markup=await order_status.order_status_kb()
    )
