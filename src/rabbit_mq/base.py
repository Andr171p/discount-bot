import aio_pika
from aio_pika.abc import (
    AbstractRobustConnection,
    AbstractRobustChannel
)

from typing import Optional

from src.rabbit_mq.exc import RabbitException
from src.config import settings


class RabbitBase:
    def __init__(
            self,
            url: str = settings.rabbit.url
    ) -> None:
        self._url = url
        self._connection: Optional[AbstractRobustConnection] = None
        self._channel: Optional[AbstractRobustChannel] = None

    async def connect(self) -> AbstractRobustConnection:
        try:
            self._connection = await aio_pika.connect_robust(self._url)
            return self._connection
        except Exception as _ex:
            raise RabbitException(_ex)

    async def channel(self) -> AbstractRobustChannel:
        if not self._connection or self._connection.is_closed:
            await self.connect()
        if not self._channel or self._channel.is_closed:
            self._channel = await self._connection.channel()
        return self._channel

    async def close(self) -> None:
        if self._channel and not self._channel.is_closed:
            await self._channel.close()
        if self._connection and not self._connection.is_closed:
            await self._connection.close()

    async def __aenter__(self) -> "RabbitBase":
        await self.connect()
        self._channel = await self.channel()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        await self.close()
