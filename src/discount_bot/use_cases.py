from .schemas import User, Order
from .base import ClientService, CrudRepository


class RegistrationUseCase:
    def __init__(self, user_repository: CrudRepository[User]) -> None:
        self._user_repository = user_repository

    async def execute(self, user: User) -> None:
        existing_user = await self._user_repository.read(user.id)
        if existing_user:
            return
        await self._user_repository.create(user)


class ReceivingOrdersUseCase:
    def __init__(
            self,
            client_service: ClientService,
            user_repository: CrudRepository[User]
    ) -> None:
        self._client_service = client_service
        self._user_repository = user_repository

    async def execute(self, id: int) -> list[Order]:
        user = await self._user_repository.read(id)
        orders = await self._client_service.get_orders(user.phone)
        return orders
