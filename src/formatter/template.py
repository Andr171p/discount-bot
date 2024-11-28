from typing import Any, Dict

from src.formatter.statuses import Statuses
from src.utils import load_json
from src.config import config


async def get_message(order: Dict[str, Any]) -> str:
    templates = await load_json(path=config.messages.statuses)
    '''text = templates[order['status']].format(
        number=order['number'],
        date=order['date'],
        amount=order['amount'],
        pay_status=order['pay_status'],
        cooking_time_from=order['cooking_time_from'],
        cooking_time_to=order['cooking_time_to'],
        delivery_time_from=order['delivery_time_from'],
        delivery_time_to=order['delivery_time_to'],
        trade_point=order['trade_point'],
        trade_point_card=order['trade_point_card'],
        delivery_adress=order['delivery_adress']
    )'''
    text = templates[order['status']].format(**order)
    print(text)


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
asyncio.run(get_message(order=order.model_dump()))
