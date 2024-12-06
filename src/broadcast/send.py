from src.app.bot import bot
from src.app.schemas.order import OrderSchema
from src.message.order_status import OrderStatus


async def send_order_status(user_id: int, order: OrderSchema) -> None:
    order_status = OrderStatus(order=order)
    bot_message = await order_status.get_bot_message(user_id=user_id)
    await bot.send_message(
        chat_id=bot_message.user_id,
        text=bot_message.text,
        reply_markup=bot_message.keyboard
    )
