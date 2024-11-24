from sqlalchemy import select
from typing import Sequence

from src.database.services.db import DBSession
from src.database.models.user import UserModel


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
        return user

    async def update_user(self, user: UserModel) -> UserModel | None:
        async with self.session() as session:
            await session.merge(user)
            await session.commit()
            await session.refresh(user)
        return user

    async def delete_user(self, user_id: int) -> UserModel:
        async with self.session() as session:
            user = await session.execute(
                select(UserModel).where(UserModel.user_id == user_id)
            )
            if user:
                await session.delete(user)
                await session.commit()
            return user.scalars().one()

    async def get_user(self, user_id: int) -> UserModel | None:
        async with self.session() as session:
            user = await session.execute(
                select(UserModel).where(UserModel.user_id == user_id)
            )
            return user.scalars().one()

    async def get_users(self) -> Sequence[UserModel]:
        async with self.session() as session:
            users = await session.execute(
                select(UserModel)
            )
            return users.scalars().all()


user_service = UserService()
