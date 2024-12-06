from src.app.bot import bot
from src.app.schemas.order import OrderSchema
from src.app.keyboards.status import pay_link_kb
from src.formatter.message import get_message


async def send_order_status(user_id: int, order: OrderSchema) -> None:
    text: str = await get_message(order=order.model_dump())
    if order.pay_status != "CONFIRMED" and order.status not in ("Завершен", "Отменен"):
        if order.delivery_method != "Курьер":
            await bot.send_message(
                chat_id=user_id,
                text="Ваш заказ №{number} ПРИНЯТ время готовности {cooking_time_to} дата {date} г. по адресу: {trade_point_card}".format(**order.model_dump()),
                reply_markup=await pay_link_kb(url=order.pay_link)
            )
        else:
            await bot.send_message(
                chat_id=user_id,
                text=text,
                reply_markup=await pay_link_kb(url=order.pay_link)
            )
    else:
        if order.delivery_method != "Курьер":
            await bot.send_message(
                chat_id=user_id,
                text="Ваш заказ №{number} ПРИНЯТ время готовности {cooking_time_to} дата {date} г. по адресу: {trade_point_card}\nОПЛАЧЕН".format(**order.model_dump()),
            )
        else:
            await bot.send_message(
                chat_id=user_id,
                text=f"{text}\nОПЛАЧЕН"
            )
