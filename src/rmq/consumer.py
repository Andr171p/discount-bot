import aio_pika
from aio_pika.abc import AbstractIncomingMessage

from src.config import config

import asyncio


async def process_message(message: AbstractIncomingMessage) -> None:
    async with message.process():
        # logging message ...
        print(f"[x] Received [{message.body.decode()}]")
        await message.ack()


async def consume(
        routing_key: str = config.queue.name
) -> ...:
    connection = await aio_pika.connect_robust(
        url=config.rmq.url
    )
    async with connection:
        channel = await connection.channel()
        queue = await channel.declare_queue(name=routing_key)
        await queue.consume(process_message)
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(consume(routing_key=config.queue.name))
