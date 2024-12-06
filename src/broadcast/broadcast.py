from src.rmq import consumer
from src.broadcast.process import process_message
from src.config import config


async def run_rmq_broadcast() -> None:
    await consumer.consume(
        callback=process_message,
        routing_key=config.queue.name
    )
