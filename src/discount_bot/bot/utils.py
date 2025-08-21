from typing import Any

from aiogram.types import InlineKeyboardMarkup

from .templates import *
from .keyboards import payment_kb, confirmed_payment_kb

from ..schemas import Order, OrderStatus, DeliveryMethod

STATUS_TEMPLATES: dict[OrderStatus, str] = {
    (OrderStatus.ACCEPTED_BY_OPERATOR, DeliveryMethod.COURIER): ACCEPTED_BY_OPERATOR_AND_COURIER_DELIVERY,
    (OrderStatus.ACCEPTED_BY_OPERATOR, DeliveryMethod.PICKUP): ACCEPTED_BY_OPERATOR_AND_CLIENT_PICKUP,
    OrderStatus.TRANSFERRED_TO_KITCHEN: TRANSFERRED_TO_KITCHEN,
    OrderStatus.COOKING: COOKING,
    OrderStatus.PREPARED: PREPARED,
    OrderStatus.READY_FOR_PICKUP: READY_FOR_PICKUP,
    OrderStatus.TRANSFERRED_TO_COURIER: TRANSFERRED_TO_COURIER,
    OrderStatus.DELIVERED: DELIVERED,
    OrderStatus.FINISHED: FINISHED,
    OrderStatus.CANCELED: CANCELED,
}

CONFIRMED = "CONFIRMED"


class Order2MessageConverter:
    def __init__(self, order: Order) -> None:
        self.order = order

    def _to_text(self) -> str:
        template = STATUS_TEMPLATES.get((self.order.status, self.order.delivery_method))
        if not template:
            template = STATUS_TEMPLATES.get(self.order.status)
        if template is None:
            raise ValueError(f"Not template defined for status: {self.order.status}")
        return template.format(**self.order.model_dump())

    def _to_keyboard(self) -> InlineKeyboardMarkup:
        if self.order.pay_status == CONFIRMED:
            return confirmed_payment_kb(self.order.pay_link)
        return payment_kb(self.order.pay_link)

    def convert(self) -> dict[str, Any]:
        return {
            "text": self._to_text(),
            "reply_markup": self._to_keyboard()
        }
