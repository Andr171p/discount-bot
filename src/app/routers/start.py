from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command


start_router = Router()


@start_router.message(Command("start"))
async def start(message: Message) -> None:
    user_id: int = message.from_user.id
    username: str = message.from_user.username
    await message.answer(
        text="Здравствуйте, {username}! Вам нужно пройти регистрацию. Это займёт всего пару секунд"
    )
