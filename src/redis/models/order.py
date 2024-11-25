from aredis_om.model import Field, JsonModel
from typing import Self


class OrderModel(JsonModel):
    client: str
    number: str = Field(index=True)
    date: str
    status: str = Field(index=True)
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
    phone: str = Field(index=True)
    timestamp: int

    def __eq__(self, other: Self) -> bool:
        if not isinstance(other, OrderModel):
            return False

        return all(
            getattr(self, attr) == getattr(other, attr)
            for attr in self.__dataclass_fields__
        )

    def __ne__(self, other: Self) -> bool:
        return not self.__eq__(other)
