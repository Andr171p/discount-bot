import json
from aio_pika.abc import AbstractIncomingMessage

from src.app.bot import bot
from src.broadcast.models.message import OrderSchema
from src.database.services.service import user_service


async def process_message(message: AbstractIncomingMessage) -> None:
    async with message.process():
        # logging message ...
        print(f"[x] Received [{message.body.decode()}]")
        data: str = message.body.decode()
        order = OrderSchema.parse_raw(json.loads(data))
        await message.ack()
