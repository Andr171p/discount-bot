import json
from typing import List
from aio_pika.abc import AbstractIncomingMessage

from src.app.bot import bot
from src.broadcast.models.order import OrderSchema
from src.database.services.service import user_service
from src.formatter.message import get_message


async def process_message(message: AbstractIncomingMessage) -> None:
    async with message.process():
        # logging message ...
        print(f"[x] Received [{message.body.decode()}]")
        # data: str = json.loads(message.body.decode())
        data: str = message.body.decode()
        order = OrderSchema.parse_raw(data)
        phones: List[str] = order.phones
        for phone in phones:
            user = await user_service.get_user(phone)
            user_id: int = user.user_id
            text: str = await get_message(order=order.model_dump())
            try:
                await bot.send_message(
                    chat_id=user_id,
                    text=text
                )
            except Exception as _ex:
                # logging exception ...
                raise _ex
            finally:
                await message.ack()
