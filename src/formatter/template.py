'''from typing import Any, Dict

from src.utils import load_json
from src.config import config


async def get_message(order: Dict[str, Any]) -> str:
    messages = await load_json(path=config.messages.statuses)
    return messages[order['status']].format(**order)


import asyncio
from src.broadcast.models.order import OrderSchema
order = OrderSchema(
    client="bob",
    number="12345",
    date="77-77-77",
    status="Готов для выдачи",
    amount=1000,
    pay_link="https://big-dick.ru",
    pay_status="CONFIRMED",
    cooking_time_from="10-00-99",
    cooking_time_to="11-00-99",
    delivery_time_from="12-00-99",
    delivery_time_to="12-00-99",
    project="Сушеф.рф",
    trade_point="LA",
    trade_point_card="----------",
    delivery_method="Курьер",
    delivery_adress="OOP 82 k1",
    phones=["+7(800)555-35-35"]
)
asyncio.run(get_message(order=order.model_dump()))'''
