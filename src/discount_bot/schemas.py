from typing import Optional

from enum import StrEnum
from datetime import datetime

from pydantic import BaseModel, field_validator, ConfigDict, Field

from .utils import format_phone, parse_order_number
from .constants import MIN_AMOUNT, PROJECT


class User(BaseModel):
    id: int
    username: Optional[str]
    phone: str
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)

    @field_validator("phone")
    def validate_phone(cls, phone: str) -> str:
        return format_phone(phone)


class PayStatus(StrEnum):
    CONFIRMED = "CONFIRMED"  # Оплачен


class OrderStatus(StrEnum):
    ACCEPTED_BY_OPERATOR = "Принят оператором"
    READY_FOR_PICKUP = "Готов для выдачи"
    COOKING = "Готовится"
    DELIVERED = "Доставлен"
    FINISHED = "Завершен"
    CANCELED = "Отменен"
    TRANSFERRED_TO_COURIER = "Передан курьеру"
    TRANSFERRED_TO_KITCHEN = "Передан на кухню"
    PREPARED = "Приготовлен"
    PACKED = "Укомплектован"


class DeliveryMethod(StrEnum):
    COURIER = "Курьер"
    PICKUP = "Самовывоз"


class Order(BaseModel):
    client: str                           # ФИО клиента
    number: str                           # Номер заказа
    date: str                             # Дата заказа
    status: OrderStatus                   # Статус заказа
    amount: float = Field(ge=MIN_AMOUNT)  # Сумма заказа в руб
    pay_link: str                         # Ссылка на оплату
    pay_status: str                       # Статус оплаты
    cooking_time_from: str                # Ближайшее время приготовления
    cooking_time_to: str                  # Крайнее время приготовления
    delivery_time_from: str               # Ближайшее время доставки
    delivery_time_to: str                 # Крайнее время доставки
    project: str                          # Какому сервису принадлежит заказ
    trade_point: str                      # Филиал, который готовит заказ
    trade_point_card: str                 # Адрес филиала
    delivery_method: DeliveryMethod       # Способ доставки
    delivery_adress: str                  # Адрес доставки
    phones: list[str]                     # Прикреплённые номера телефонов

    model_config = ConfigDict(from_attributes=True)

    @field_validator("project")
    def validate_project(cls, project: str) -> str:
        if project != PROJECT:
            raise ValueError("Incorrect project")
        return project

    @field_validator("number")
    def validate_number(cls, number: str) -> str:
        return parse_order_number(number)

    @field_validator(
        "date",
        "cooking_time_from",
        "cooking_time_to",
        "delivery_time_from",
        "delivery_time_to"
    )
    def validate_timings(cls, timing: str) -> datetime:
        return datetime.fromisoformat(timing)
