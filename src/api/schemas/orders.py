from typing import List
from pydantic import BaseModel

from src.api.schemas.order import OrderSchema


class OrdersSchema(BaseModel):
    orders: List[OrderSchema]
