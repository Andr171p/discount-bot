from sqlalchemy.orm import DeclarativeBase

from src.config import settings


DB_URL: str = settings.pg.url


class Base(DeclarativeBase):
    pass
