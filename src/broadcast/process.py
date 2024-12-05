from typing import List
from aio_pika.abc import AbstractIncomingMessage

from src.app.bot import bot
from src.app.keyboards.status import pay_link_kb
from src.app.schemas.order import OrderSchema
from src.broadcast.logger import logger
from src.database.services.service import user_service
from src.formatter.message import get_message


async def process_message(message: AbstractIncomingMessage) -> None:
    async with message.process():
        data: str = message.body.decode()
        logger.info(f"[x] Received: [{data}]")
        order = OrderSchema.parse_raw(data)
        print(order)
        phones: List[str] = order.phones
        for phone in phones:
            # phone = format_phone(phone=phone)
            user = await user_service.get_user(phone)
            if user is not None:
                user_id: int = user.user_id
            text: str = await get_message(order=order.model_dump())
            logger.info(text)
            try:
                if order.pay_status != "CONFIRMED":
                    await bot.send_message(
                        chat_id=user_id,
                        text=text,
                        reply_markup=await pay_link_kb(url=order.pay_link)
                    )
                else:
                    await bot.send_message(
                        chat_id=user_id,
                        text=text
                    )
                logger.info(f"message sent to user_id=[{user_id}] successfully")
            except Exception as _ex:
                logger.warning(_ex)
                logger.warning(f"message was not sent")
            finally:
                await message.ack()
