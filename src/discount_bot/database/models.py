from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class UserOrm(Base):
    __tablename__ = "users"

    username: Mapped[str | None] = mapped_column(nullable=True)
    phone: Mapped[str] = mapped_column(unique=True)
