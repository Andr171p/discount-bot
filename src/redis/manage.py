from typing import Dict

from src.config import config
from src.utils import timestamp
from src.redis.service import RedisConnection


class RedisManager(RedisConnection):
    async def is_exists(self, number: str) -> bool:
        return await self._connection.exists(number)

    async def is_unique(
            self,
            number: str,
            status: str
    ) -> bool:
        redis_status: str = await self._connection.hget(
            name=number,
            key="status"
        )
        return redis_status.decode("utf-8") != status

    async def set_order(self, order: Dict[str, str]) -> None:
        data = {
            "timestamp": timestamp(),
            "phone": order["phone"],
            "pay_link": order["pay_link"],
            "project": order["project"],
            "status": order["status"],
            "message": order["message"]
        }
        await self._connection.hset(
            name=order["number"],
            mapping=data
            )

    async def add_order(self, order: Dict[str, str]) -> None:
        async with self.connection() as connection:
            if await self.is_exists(number=order["number"]):
                if not await self.is_unique(number=order["number"], status=order["status"]):
                    return
                await connection.delete(order["number"])
            await self.set_order(order=order)
            await connection.expire(order["number"], config.storage.expire_timeout)
