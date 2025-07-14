import logging

import aiohttp

from .schemas import Order
from .base import ClientService
from .exceptions import ServiceError, RequestFailed
from .constants import PROJECT

logger = logging.getLogger(__name__)

STATUS_200_OK = 200


class APIClientService(ClientService):
    def __init__(self, base_url: str) -> None:
        self.base_url = base_url

    async def get_orders(self, phone: str) -> list[Order]:
        headers: dict[str, str] = {"Content-Type": "application/json; charset=UTF-8"}
        payload: dict[str, str] = {"command": "status", "telefon": phone}
        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(
                        url=self.base_url, headers=headers, json=payload
                ) as response:
                    if response.status != STATUS_200_OK:
                        raise RequestFailed(f"Request failed with status: {response.status}")
                    data = await response.json()
            orders = data["data"]["orders"]
            return [
                Order.model_validate(order)
                for order in orders
                if order["project"] == PROJECT
            ]
        except aiohttp.ClientError as e:
            logger.error("Error while receiving orders", str(e))
            raise ServiceError(f"Error while receiving orders: {e}") from e
