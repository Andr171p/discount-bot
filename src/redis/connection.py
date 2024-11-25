import contextlib
import redis.asyncio as aioredis
from typing import AsyncGenerator, Optional, TypeVar

from src.config import config


T = TypeVar("T")


class RedisConnection:
    def __init__(self) -> None:
        self._connection: Optional[aioredis.Redis] = None

    async def connect(
            self,
            host: str = config.storage.host,
            port: int = config.storage.port,
    ) -> aioredis.Redis | None:
        url = f"redis://{host}:{port}"
        self._connection = await aioredis.from_url(url=url)
        return self._connection

    async def close(self) -> None:
        if self._connection:
            await self._connection.aclose()
            self._connection = None

    @contextlib.asynccontextmanager
    async def connection(self) -> AsyncGenerator[aioredis.Redis, T]:
        await self.connect()
        try:
            yield self._connection
        finally:
            await self.close()
