from typing import TYPE_CHECKING

from aio_pika import ExchangeType
from aio_pika.abc import AbstractRobustQueue

from src.rabbit_mq.exc import RabbitException
from src.config import settings


if TYPE_CHECKING:
    from aio_pika.abc import AbstractRobustChannel


class RabbitExchange:
    _channel: "AbstractRobustChannel"

    async def declare_exchange(self) -> None:
        if self._channel is None:
            raise RabbitException("Channel must be initialized first")
        await self._channel.declare_exchange(
            name=settings.rabbit.queue_name,
            type=ExchangeType.FANOUT,
        )

    async def declare_bind_queue(
            self,
            queue_name: str = "",
            exclusive: bool = True
    ) -> AbstractRobustQueue:
        await self.declare_exchange()
        queue = await self._channel.declare_queue(
            name=queue_name,
            exclusive=exclusive
        )
        await queue.bind(settings.rabbit.queue_name)
        return queue
