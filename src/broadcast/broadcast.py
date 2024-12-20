from src.rabbit_mq import RabbitConsumer
from src.broadcast.process import process_message
from src.config import settings

import asyncio


async def start_rabbit_broadcast() -> None:
    async with RabbitConsumer() as consumer:
        await consumer.connect()
        await consumer.channel()
        await consumer.consume_massage(process_message)
        await asyncio.Future()
