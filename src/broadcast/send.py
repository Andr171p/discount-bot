from src.rmq import consumer
from src.broadcast.process import process_message
from src.config import config


async def send_order_status() -> None:
    await consumer.consume(
        callback=process_message,
        routing_key=config.queue.name
    )
