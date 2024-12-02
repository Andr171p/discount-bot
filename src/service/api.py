import aiohttp
from typing import Any, Dict

from src.utils import validate_phone, format_phone
from src.service.logger import logger
from src.config import config


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
                url=config.api.url,
                headers=config.api.headers,
                json=data
            ) as response:
                if is_ok(response=response):
                    return await response.json()
    except aiohttp.client_exceptions.ClientConnectorError as _ex:
        logger.critical(_ex)
