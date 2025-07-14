from typing import Generic, TypeVar, Optional

from abc import ABC, abstractmethod

from pydantic import BaseModel

from .schemas import Order, User

T = TypeVar("T", bound=BaseModel)


class ClientService(ABC):
    @abstractmethod
    async def get_orders(self, phone: str) -> list[Order]:
        """
        Метод для получения всех текущих заказов клиента по его номеру телефона.

            :param phone: Номер телефона клиента в формате 8(XXX)XXX-XX-XX или +7(XXX)XXX-XX-XX
        """
        raise NotImplementedError


class CrudRepository(Generic[T]):
    async def create(self, model: T) -> T: pass

    async def read(self, id: int) -> Optional[T]: pass

    async def read_all(self) -> list[T]: pass

    async def update(self, id: int, **kwargs) -> Optional[T]: pass

    async def delete(self, id: int) -> bool: pass


class UserRepository(CrudRepository[User]):
    async def get_by_phone(self, phone: str) -> Optional[User]: pass
