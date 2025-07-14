from datetime import datetime

from sqlalchemy import BigInteger, func
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.ext.asyncio import (
    AsyncAttrs,
    AsyncSession,
    create_async_engine,
    async_sessionmaker
)

POOL_SIZE = 10
MAX_OVERFLOW = 20
POOL_RECYCLE = 3600


class Base(AsyncAttrs, DeclarativeBase):
    __abstract__ = True

    id: Mapped[int] = mapped_column(BigInteger, autoincrement=True, primary_key=True)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())


def create_sessionmaker(url: str) -> async_sessionmaker[AsyncSession]:
    engine = create_async_engine(
        url=url,
        pool_size=POOL_SIZE,
        max_overflow=MAX_OVERFLOW,
        pool_recycle=POOL_RECYCLE,
        pool_pre_ping=True
    )
    return async_sessionmaker(
        engine,
        class_=AsyncSession,
        autoflush=False,
        expire_on_commit=False
    )
