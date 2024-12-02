from typing import Any, Dict

from src import utils
from src.config import config
from src.broadcast.models.order import OrderSchema


async def get_message(order: Dict[str, Any]) -> str:
    order = OrderSchema(**order)
    messages = await utils.load_json(path=config.messages.statuses)
    return messages[order.status].format(**order.__dict__)
