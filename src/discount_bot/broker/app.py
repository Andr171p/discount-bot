from faststream import FastStream
from faststream.rabbit import RabbitBroker
from dishka.integrations.faststream import setup_dishka

from .router import orders_router

from ..dependencies import container


async def create_faststream_app() -> FastStream:
    broker = await container.get(RabbitBroker)
    broker.include_router(orders_router)
    app = FastStream(broker)
    setup_dishka(container=container, app=app, auto_inject=True)
    return app
