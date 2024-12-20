import logging
import asyncio
from typing import Callable, Awaitable, Any

from aio_pika.abc import AbstractIncomingMessage


from src.rabbit_mq.client import RabbitClient


log = logging.getLogger(__name__)


class RabbitConsumer(RabbitClient):
    async def consume_massage(
            self,
            message_callback: Callable[[AbstractIncomingMessage], Awaitable[Any]],
            queue_name: str = "",
            prefetch_count: int = 1
    ) -> None:
        await self._channel.set_qos(prefetch_count=prefetch_count)
        queue = await self.declare_bind_queue(
            queue_name=queue_name,
            exclusive=not queue_name
        )
        await queue.consume(message_callback)
        log.info("Start consuming message")
        await asyncio.Future()
