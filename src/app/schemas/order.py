from pydantic import BaseModel, field_validator
from typing import List, Optional

from src import utils


class OrderSchema(BaseModel):
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

    @field_validator("number")
    @classmethod
    def validate_number(cls, v: str) -> str:
        return utils.format_number(v)

    @field_validator("date")
    @classmethod
    def validate_date(cls, v: str) -> str:
        return utils.format_date(v)

    @field_validator(
        "cooking_time_from",
        "cooking_time_to",
        "delivery_time_from",
        "delivery_time_to"
    )
    @classmethod
    def validate_time(cls, v: str) -> str:
        return utils.format_time(v)

    @field_validator("phones")
    @classmethod
    def validate_phones(cls, values: List[str]) -> List[str]:
        phones: Optional[List[str]] = []
        for phone in values:
            phone = utils.format_phone(phone)
            phones.append(phone)
        return phones

