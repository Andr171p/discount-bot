import asyncio
import logging

from aiogram import Bot

from src.discount_bot.bot.dispatcher import create_dispatcher
from src.discount_bot.broker.app import create_faststream_app
from src.discount_bot.dependencies import container


async def start_bot() -> None:
    bot = await container.get(Bot)
    dp = create_dispatcher()
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


async def start_broker() -> None:
    faststream_app = await create_faststream_app()
    await faststream_app.broker.start()


async def main() -> None:
    await asyncio.gather(start_bot(), start_broker())


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
