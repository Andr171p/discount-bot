from typing import Any, Dict

from src.utils import load_json
from src.config import config


async def get_message(order: Dict[str, Any]) -> str:
    messages = await load_json(path=config.messages.statuses)
    return messages[order['status']].format(**order)
