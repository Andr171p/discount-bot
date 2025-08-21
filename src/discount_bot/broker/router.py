from faststream import Logger
from faststream.rabbit import RabbitRouter, RabbitExchange, ExchangeType

from dishka.integrations.base import FromDishka as Depends

from aiogram import Bot

from ..schemas import Order
from ..base import UserRepository
from ..bot.utils import Order2MessageConverter
from ..utils import format_phone

orders_router = RabbitRouter()

exchange = RabbitExchange("orders", type=ExchangeType.FANOUT)


@orders_router.subscriber("discount-orders", exchange=exchange)
async def send_order(
        order: Order,
        user_repository: Depends[UserRepository],
        bot: Depends[Bot],
        logger: Logger
) -> None:
    try:
        for phone in order.phones:
            formatted_phone = format_phone(phone)
            user = await user_repository.get_by_phone(formatted_phone)
            converter = Order2MessageConverter(order)
            message_params = converter.convert()
            await bot.send_message(**message_params, chat_id=user.id)
    except Exception as e:
        logger.error("Error occurred", str(e))
