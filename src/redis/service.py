from datetime import datetime
from redis.asyncio import Redis
from aredis_om import get_redis_connection
from typing import Optional

from src.redis.models.order import OrderModel
from src.config import config


class OrderRedisService:
    def __init__(self) -> None:
        self._connection: Optional[Redis] = None

    def connect(
            self,
            host: str = config.redis.host,
            port: int = config.redis.port
    ) -> Redis:
        url: str = f"redis://{host}:{port}"
        self._connection = get_redis_connection(
            url=url,
            decode_responses=True
        )
        return self._connection

    async def add_order(
            self,
            order:
            OrderModel,
            ttl: int = 86400
    ) -> OrderModel:
        connection = self.connect()
        order.timestamp = int(datetime.now().timestamp())
        await order.save()
        await connection.expire(order.number, ttl)
        return order

    async def get_order(self, number: str) -> OrderModel:
        connection = self.connect()
        order = await OrderModel.find(OrderModel.number == number).first()
        return order

    async def update_order(self, order: OrderModel) -> ...:
        connection = self.connect()
        redis_order = await OrderModel.find(OrderModel.number == order.number).first()
        if redis_order is None:
            await order.save()
        else:
            for field, value in order.dict():
                setattr(redis_order, field, value)
            await redis_order.save()