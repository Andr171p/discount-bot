from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import BigInteger
from typing import TypeVar

from src.database.base import Base


class AbstractBase(AsyncAttrs, Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        autoincrement=True,
        primary_key=True
    )


ModelType = TypeVar(
    name="ModelType",
    bound=AbstractBase
)


class UserModel(AbstractBase):
    user_id: Mapped[int] = mapped_column(BigInteger)
    username: Mapped[str]
    phone: Mapped[str]

    def __repr__(self) -> str:
        return f"User(user_id={self.user_id}, username={self.username}, phone={self.phone}"