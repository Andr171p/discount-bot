
ACCEPTED_BY_OPERATOR_AND_COURIER_DELIVERY = """Ваш заказ №{number} <b>ПРИНЯТ</b> и будет
доставлен {date} с {delivery_time_from} до {delivery_time_to} по адресу {delivery_adress}.
Сумма: {amount} руб.
"""

ACCEPTED_BY_OPERATOR_AND_CLIENT_PICKUP = """Ваш заказ №{number} <b>ПРИНЯТ</b> время готовности {delivery_time_from} дата {date} г. по адресу: {trade_point_card}
"""

TRANSFERRED_TO_KITCHEN = "Ваш заказ №{number} <b>ПЕРЕДАН НА КУХНЮ</b>..."

COOKING = """Ваш заказ №{number} <b>ГОТОВИТСЯ</b>
готовность 30%"""

PREPARED = """Ваш заказ №{number} <b>ГОТОВИТСЯ</b>
готовность 50%"""

PACKED = """Ваш заказ №{number} <b>ГОТОВИТСЯ</b>
готовность 80%"""

TRANSFERRED_TO_COURIER = """Ваш заказ №{number} <b>ПЕРЕДАН КУРЬЕРУ</b>.
Ожидайте доставку с {delivery_time_from} до {delivery_time_to}
Сумма {amount}"""

DELIVERED = """Ваш заказ №{number} <b>ДОСТАВЛЕН</b> курьером.
Спасибо, сто воспользовались услугами нашего сервиса."""

READY_FOR_PICKUP = """Ваш заказ {number} <b>ГОТОВ</b>
ожидает Вас по адресу:
{trade_point_card}"""

FINISHED = """Ваш заказ №{number} успешно <b>ЗАВЕРШЁН</b>. Спасибо,  что
воспользовались услугами нашего сервиса."""

CANCELED = """Ваш заказ №{number} <b>ОТМЕНЁН</b>.
Нам очень жаль. Надеемся, на скорую встречу."""
