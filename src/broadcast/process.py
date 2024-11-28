import json
from typing import List
from aio_pika.abc import AbstractIncomingMessage

from src.app.bot import bot
from src.broadcast.models.order import OrderSchema
from src.database.services.service import user_service
from src.formatter.message import get_order_text


async def process_message(message: AbstractIncomingMessage) -> None:
    async with message.process():
        # logging message ...
        # print(f"[x] Received [{message.body.decode()}]")
        data: str = json.loads(message.body.decode())
        order = OrderSchema.parse_raw(data)
        phones: List[str] = order.phones
        for phone in phones:
            user = await user_service.get_user(phone=phone)
            user_id: int = user.user_id
            try:
                await bot.send_message(
                    chat_id=user_id,
                    text=get_order_text(order=order.model_dump())
                )
            except Exception as _ex:
                # logging exception ...
                raise _ex
            finally:
                await message.ack()
