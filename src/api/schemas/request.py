from pydantic import BaseModel

from src.config import config


class OrderRequestSchema(BaseModel):
    command: str = config.api.order
    telefon: str


class OrdersRequestSchema(BaseModel):
    command: str = config.api.orders
    active: str = "true"
