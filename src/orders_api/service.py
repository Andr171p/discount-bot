import logging
import aiohttp
from typing import Any, Dict

from src.utils import validate_phone, format_phone
from src.config import settings


log = logging.getLogger(__name__)


def is_ok(response: aiohttp.ClientResponse) -> bool:
    return True if response.status == 200 else False


async def get_user_orders(phone: str) -> Dict[str, Any]:
    if not validate_phone(phone=phone):
        phone = format_phone(phone=phone)
    data: Dict[str, str] = {
        "command": "status",
        "telefon": phone
    }
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(
                url=settings.orders_api.url,
                headers=settings.orders_api.headers,
                json=data
            ) as response:
                if is_ok(response=response):
                    return await response.json()
    except aiohttp.client_exceptions.ClientConnectorError as _ex:
        log.critical(_ex)


import asyncio
print(asyncio.run(get_user_orders("+7(919)935-09-14")))