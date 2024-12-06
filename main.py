import asyncio

from src.app.bot import run_aiogram_bot
from src.broadcast.broadcast import run_rmq_broadcast


async def main() -> None:
    await asyncio.gather(
        run_aiogram_bot(),
        run_rmq_broadcast()
    )


if __name__ == "__main__":
    asyncio.run(main())
