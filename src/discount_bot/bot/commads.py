from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot) -> None:
    commands: list[BotCommand] = [
        BotCommand(command="start", description="Перезапустить бота"),
        BotCommand(command="orders", description="Узнать статус заказа")
    ]
    await bot.set_my_commands(
        commands=commands,
        scope=BotCommandScopeDefault()
    )
