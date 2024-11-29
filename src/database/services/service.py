from sqlalchemy import select
from typing import Any, Sequence
from functools import singledispatchmethod

from src.database.services.db import DBSession
from src.database.models.user import UserModel
from src.database.logger import logger


class UserService(DBSession):
    def __init__(self) -> None:
        super().__init__()
        self.init()

    async def create_users(self) -> None:
        async with self.connect() as connection:
            await connection.run_sync(UserModel.metadata.drop_all)
            await connection.run_sync(UserModel.metadata.create_all)

    async def add_user(self, user: UserModel) -> UserModel | None:
        async with self.session() as session:
            session.add(user)
            await session.commit()
            await session.refresh(user)
            logger.debug(f"user: {user} add to `users` successfully")
        return user

    async def update_user(self, user: UserModel) -> UserModel | None:
        async with self.session() as session:
            await session.merge(user)
            await session.commit()
            await session.refresh(user)
            logger.debug(f"user: {user} updated successfully")
        return user

    async def delete_user(self, user_id: int) -> UserModel:
        async with self.session() as session:
            user = await session.execute(
                select(UserModel).where(UserModel.user_id == user_id)
            )
            if user:
                await session.delete(user)
                await session.commit()
                logger.debug(f"user: {user} deleted successfully")
            return user.scalars().one()

    @singledispatchmethod
    async def get_user(self, arg: Any) -> UserModel | None:
        raise NotImplementedError("<UserService> `get_user` method not implement...")

    @get_user.register
    async def _(self, user_id: int) -> UserModel | None:
        async with self.session() as session:
            user = await session.execute(
                select(UserModel).where(UserModel.user_id == user_id)
            )
            try:
                return user.scalars().one()
            except Exception as _ex:
                logger.warning(_ex)
                logger.warning("user not found")
                return

    @get_user.register
    async def _(self, phone: str) -> UserModel | None:
        async with self.session() as session:
            user = await session.execute(
                select(UserModel).where(UserModel.phone == phone)
            )
            try:
                return user.scalars().one()
            except Exception as _ex:
                logger.warning(_ex)
                logger.warning("user not found")
                return

    async def get_users(self) -> Sequence[UserModel]:
        async with self.session() as session:
            users = await session.execute(
                select(UserModel)
            )
            return users.scalars().all()


user_service = UserService()
