from src.app.bot import Bot
from src.rmq.consumer import consume
from src.broadcast.process import process_message


async def broadcast(bot: Bot) -> None:
    async with Bot as bot:
        async def process_message(message):
            ...
