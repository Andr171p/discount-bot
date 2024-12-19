from src.rabbit_mq.base import RabbitBase
from src.rabbit_mq.exchange import RabbitExchange


class RabbitClient(RabbitExchange, RabbitBase):
    pass
