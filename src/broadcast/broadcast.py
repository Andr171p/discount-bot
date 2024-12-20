from src.rabbit_mq import RabbitConsumer
from src.broadcast.process import process_message
from src.config import settings

import asyncio


async def start_rabbit_broadcast() -> None:
    async with RabbitConsumer() as consumer:
        await consumer.consume_massage(
            message_callback=process_message,
            queue_name=settings.rabbit.project_queue_name
        )
