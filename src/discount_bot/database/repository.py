from typing import Optional

from sqlalchemy import insert, select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from .models import UserOrm

from ..schemas import User
from ..base import UserRepository
from ..exceptions import CreationError, ReadingError


class SQLUserRepository(UserRepository):
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def create(self, user: User) -> User:
        try:
            stmt = (
                insert(UserOrm)
                .values(**user.model_dump())
                .returning(UserOrm)
            )
            result = await self.session.execute(stmt)
            await self.session.commit()
            user = result.scalar_one()
            return User.model_validate(user)
        except SQLAlchemyError as e:
            await self.session.rollback()
            raise CreationError(f"Error while user creation: {e}") from e

    async def read(self, id: int) -> Optional[User]:
        try:
            stmt = (
                select(UserOrm)
                .where(UserOrm.id == id)
            )
            result = await self.session.execute(stmt)
            user = result.scalar_one_or_none()
            return User.model_validate(user) if user else None
        except SQLAlchemyError as e:
            await self.session.rollback()
            raise ReadingError(f"Error while user reading: {e}") from e

    async def get_by_phone(self, phone: str) -> Optional[User]:
        try:
            stmt = (
                select(UserOrm)
                .where(UserOrm.phone == phone)
            )
            result = await self.session.execute(stmt)
            user = result.scalar_one_or_none()
            return User.model_validate(user) if user else None
        except SQLAlchemyError as e:
            await self.session.rollback()
            raise ReadingError(f"Error while reading by phone: {e}") from e
