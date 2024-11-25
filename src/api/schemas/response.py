from typing import List
from pydantic import BaseModel


class OrderResponseSchema(BaseModel):
    client: str
    number: str
    date: str
    status: str
    amount: float
    pay_link: str
    pay_status: str
    cooking_time_from: str
    cooking_time_to: str
    delivery_time_from: str
    delivery_time_to: str
    project: str
    trade_point: str
    trade_point_card: str
    delivery_method: str
    delivery_adress: str
    phones: List[str]


class OrdersResponseSchema(BaseModel):
    orders: List[OrderResponseSchema]
