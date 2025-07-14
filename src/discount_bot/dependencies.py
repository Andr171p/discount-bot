from collections.abc import AsyncIterable

from dishka import Provider, provide, Scope, from_context, make_async_container

from aiogram import Bot
from aiogram.enums.parse_mode import ParseMode
from aiogram.client.default import DefaultBotProperties

from faststream.rabbit import RabbitBroker

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from .base import ClientService, UserRepository
from .use_cases import RegistrationUseCase, ReceivingOrdersUseCase

from .rest import APIClientService

from .database.base import create_sessionmaker
from .database.repository import SQLUserRepository

from .settings import Settings


class AppProvider(Provider):
    app_settings = from_context(provides=Settings, scope=Scope.APP)

    @provide(scope=Scope.APP)
    def get_bot(self, app_settings: Settings) -> Bot:
        return Bot(
            token=app_settings.bot.token,
            default=DefaultBotProperties(parse_mode=ParseMode.HTML)
        )

    @provide(scope=Scope.APP)
    def get_rabbit_broker(self, app_settings: Settings) -> RabbitBroker:
        return RabbitBroker(url=app_settings.rabbit.url)

    @provide(scope=Scope.APP)
    def get_sessionmaker(self, app_settings: Settings) -> async_sessionmaker[AsyncSession]:
        return create_sessionmaker(app_settings.postgres.url)

    @provide(scope=Scope.REQUEST)
    async def get_session(
            self,
            session_maker: async_sessionmaker[AsyncSession]
    ) -> AsyncIterable[AsyncSession]:
        async with session_maker() as session:
            yield session

    @provide(scope=Scope.REQUEST)
    def get_user_repository(self, session: AsyncSession) -> UserRepository:
        return SQLUserRepository(session)

    @provide(scope=Scope.APP)
    def get_client_service(self, app_settings: Settings) -> ClientService:
        return APIClientService(app_settings.api.url)

    @provide(scope=Scope.REQUEST)
    def get_registration_use_case(self, user_repository: UserRepository) -> RegistrationUseCase:
        return RegistrationUseCase(user_repository)

    @provide(scope=Scope.REQUEST)
    def get_receiving_orders_use_case(
            self,
            user_repository: UserRepository,
            client_service: ClientService
    ) -> ReceivingOrdersUseCase:
        return ReceivingOrdersUseCase(client_service, user_repository)


settings = Settings()

container = make_async_container(AppProvider(), context={Settings: settings})
