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

    @field_validator("delivery_adress")
    @classmethod
    def validate_adress(cls, value: str) -> str:
        return utils.format_address(value)


'''o = {
  "client": "Косов Сергей Владимирович",
  "number": "00НФ-013523",
  "date": "2024-12-01T00:00:00",
  "status": "Принят оператором",
  "amount": 10,
  "pay_link": "https://securepayments.tinkoff.ru/4J0Ek30r",
  "pay_status": "NEW",
  "cooking_time_from": "0001-01-01T00:00:00",
  "cooking_time_to": "0001-01-01T13:30:00",
  "delivery_time_from": "0001-01-01T15:00:00",
  "delivery_time_to": "0001-01-01T15:30:00",
  "project": "Дисконт Суши",
  "trade_point": "Московский тракт, 87к1",
  "trade_point_card": "MockoBcku'u TpakT 87 k.1 https://go.2gis.com/pdacd",
  "delivery_method": "Курьер",
  "delivery_adress": "625001, Тюменская обл, г.о. город Тюмень, г Тюмень, ул Полевая, д. 117, к. 2, кв. 145, подъезд 1, этаж 1",
  "phones": ["9829764729"]
}
print(OrderSchema(**o))'''