import aiohttp
from typing import Any, Dict

from src.config import config


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
    ) -> Dict:
        data: Dict[str, Any] = {
            "command": config.api.order,
            "telefon": phone
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(
                url=self.url,
                headers=self.headers,
                json=data,
                timeout=timeout
            ) as response:
                if self.is_ok(response=response):
                    return await response.json()

    async def get_orders(
            self,
            timeout: int = 10
    ) -> Dict:
        data: Dict[str, Any] = {
            "command": config.api.orders,
            "active": "true"
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(
                url=self.url,
                headers=self.headers,
                json=data,
                timeout=timeout
            ) as response:
                if self.is_ok(response=response):
                    return await response.json()

    async def get_flyers(self, phone: str) -> Dict:
        pass

    async def get_orders_history(self, phone: str) -> Dict:
        pass


import asyncio

print(asyncio.run(OrderServiceAPI().get_orders()))
from src.utils import format_phone
phone = format_phone("9526725393")
print(phone)
print(asyncio.run(OrderServiceAPI().get_order(phone=phone)))
print(asyncio.run(OrderServiceAPI().get_order(phone="89526725393")))
