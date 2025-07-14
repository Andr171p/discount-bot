import logging

from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

from dishka.integrations.aiogram import FromDishka as Depends

from .keyboards import start_kb
from .utils import Order2MessageConverter

from ..schemas import User
from ..use_cases import RegistrationUseCase, ReceivingOrdersUseCase
from ..base import UserRepository
from ..exceptions import ServiceError, CreationError

logger = logging.getLogger(__name__)

router = Router()


@router.message(CommandStart())
async def start(message: Message, user_repository: Depends[UserRepository]) -> None:
    existing_user = await user_repository.read(message.from_user.id)
    if not existing_user:
        await message.answer(f"""Здравствуйте, {message.from_user.first_name}! Вам нужно пройти регистрацию.
        Это займёт всего пару секунд.
        """, reply_markup=start_kb())
    else:
        await message.answer("Вы уже зарегистрированы")


@router.message(F.contact)
async def register_user(
        message: Message,
        registration_use_case: Depends[RegistrationUseCase]
) -> None:
    try:
        user = User(
            id=message.from_user.id,
            username=message.from_user.username,
            phone=message.contact.phone_number
        )
        await registration_use_case.execute(user)
        await message.answer("Вы успешно зарегистрированы!")
    except CreationError as e:
        logger.error("Error occurred", str(e))
        await message.answer("⚠️ Произошла ошибка при регистрации!")


@router.message(Command("orders"))
async def send_orders(
        message: Message,
        receiving_orders_use_case: Depends[ReceivingOrdersUseCase]
) -> None:
    try:
        orders = await receiving_orders_use_case.execute(message.from_user.id)
        if not orders:
            await message.answer("У Вас нет активных заказов на текущую дату")
            return
        for order in orders:
            converter = Order2MessageConverter(order)
            message_params = converter.convert()
            await message.answer(**message_params)
    except ServiceError as e:
        logger.error("Error occurred", str(e))
        await message.answer("⚠️ Произошла ошибка при получении заказа!")
