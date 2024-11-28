import asyncio
import aio_pika

from src.config import config


async def consume(
        callback: callable,
        routing_key: str = config.queue.name
) -> None:
    connection = await aio_pika.connect_robust(
        url=config.rmq.url
    )
    async with connection:
        channel = await connection.channel()
        queue = await channel.declare_queue(name=routing_key)
        await queue.consume(callback)
        await asyncio.Future()
