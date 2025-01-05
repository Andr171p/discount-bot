import asyncio

from src.app.run import run_aiogram_bot
from src.broadcast.broadcast import start_rabbit_broadcast


async def main() -> None:
    await asyncio.gather(
        run_aiogram_bot(),
        start_rabbit_broadcast()
    )


if __name__ == "__main__":
    asyncio.run(main())
