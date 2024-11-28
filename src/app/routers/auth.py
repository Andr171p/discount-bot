from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from src.config import config
from src.utils import load_json, format_phone
from src.app.keyboards import auth, status
from src.app.schemas.user import UserSchema
from src.app.states.contact import ContactForm
from src.database.models.user import UserModel
from src.database.services.service import user_service


auth_router = Router()


@auth_router.message(F.contact)
async def get_user_contact(message: Message, state: FSMContext) -> None:
    user_id: int = message.from_user.id
    username: str = message.from_user.username
    phone: str = message.contact.phone_number
    user = UserSchema(
        user_id=user_id,
        username=username,
        phone=format_phone(phone)
    )
    await state.update_data(user=user)
    text = await load_json(path=config.messages.auth)
    await message.answer(
        text=text['question'].format(phone=phone),
        reply_markup=await auth.valid_phone_kb()
    )


@auth_router.callback_query(F.data == "valid_phone")
async def create_user(callback: CallbackQuery, state: FSMContext) -> None:
    await callback.answer()
    user = await state.get_data()
    await state.clear()
    _ = await user_service.add_user(user=UserModel(**user['user'].__dict__))
    text = await load_json(path=config.messages.auth)
    await callback.message.answer(
        text=text['success'],
        reply_markup=await status.order_status_kb()
    )


@auth_router.callback_query(F.data == "invalid_phone")
async def get_phone_form(callback: CallbackQuery, state: FSMContext) -> None:
    await callback.answer()
    await state.set_state(ContactForm.phone)
    text = await load_json(path=config.messages.auth)
    await callback.message.answer(text=text['input'])


@auth_router.message(ContactForm.phone)
async def get_user_phone(message: Message, state: FSMContext) -> None:
    user_id: int = message.from_user.id
    username: str = message.from_user.username
    phone: str = message.text
    await state.clear()
    user = UserSchema(
        user_id=user_id,
        username=username,
        phone=phone
    )
    _ = await user_service.add_user(user=UserModel(**user.__dict__))
    text = await load_json(path=config.messages.auth)
    await message.answer(
        text=text['success'],
        reply_markup=await status.order_status_kb()
    )
