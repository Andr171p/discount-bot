import aiohttp
from typing import Any, Dict

from src.config import config
from src.api.schemas.request import OrderRequestSchema, OrdersRequestSchema
from src.api.schemas.response import OrderResponseSchema, OrdersResponseSchema


class OrderServiceAPI:
    def __init__(
            self,
            url: str = f"{config.api.url}{config.api.token}",
            headers: Dict[str, str] = config.api.headers
    ) -> None:
        self.url = url
        self.headers = headers

    @staticmethod
    def is_ok(response: aiohttp.ClientResponse) -> bool:
        return True if response.status == 200 else False

    async def get_order(
            self,
            phone: str,
            timeout: int = 10
    ) -> OrderResponseSchema:
        data: Dict[str, Any] = OrderRequestSchema(telefon=phone).model_dump()
        async with aiohttp.ClientSession() as session:
            async with session.post(
                url=self.url,
                headers=self.headers,
                json=data,
                timeout=timeout
            ) as response:
                if self.is_ok(response=response):
                    order = await response.json()
                    return OrderResponseSchema(**order['data']['order'])

    async def get_orders(
            self,
            timeout: int = 10
    ) -> OrdersResponseSchema:
        data: Dict[str, Any] = OrdersRequestSchema().model_dump()
        async with aiohttp.ClientSession() as session:
            async with session.post(
                url=self.url,
                headers=self.headers,
                json=data,
                timeout=timeout
            ) as response:
                if self.is_ok(response=response):
                    orders = await response.json()
                    return OrdersResponseSchema(**orders['data'])

    async def get_flyers(self, phone: str) -> Dict:
        pass

    async def get_orders_history(self, phone: str) -> Dict:
        pass
