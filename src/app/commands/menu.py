from typing import List

from aiogram.types import BotCommand, BotCommandScopeDefault

from src.app.bot import bot


async def set_commands() -> None:
    commands: List[BotCommand] = [
        BotCommand(command="start", description="Перезапустить бота"),
        BotCommand(command="orders", description="Узнать статус заказа")
    ]
    await bot.set_my_commands(
        commands=commands,
        scope=BotCommandScopeDefault()
    )
