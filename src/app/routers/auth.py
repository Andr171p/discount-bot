from aiogram import F, Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from src.config import config
from src.utils import load_json, format_phone


auth_router = Router()


@auth_router.message(F.contact)
async def get_user_contact(message: Message) -> None:
    user_id: int = message.from_user.id
    username: str = message.from_user.username
    phone: str = message.contact.phone_number
    ...
    text = await load_json(path=config.messages.auth)
    await message.answer(
        text=text['question'].format(phone=phone)
    )
