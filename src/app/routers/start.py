from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command


start_router = Router()


@start_router.message(Command("start"))
async def start(message: Message) -> None:
    await message.answer("")
