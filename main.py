import asyncio

from src.app.bot import run_aiogram_bot
from src.broadcast.send import send_order_status


async def main() -> None:
    await asyncio.gather(
        run_aiogram_bot(),
        send_order_status()
    )


if __name__ == "__main__":
    asyncio.run(main())
