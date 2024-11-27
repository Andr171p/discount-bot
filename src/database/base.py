from sqlalchemy.orm import DeclarativeBase

from src.config import config


DB_URL: str = config.postgresql.url


class Base(DeclarativeBase):
    pass
