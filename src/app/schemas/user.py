from pydantic import BaseModel, field_validator

from src.utils import validate_phone


class UserSchema(BaseModel):
    user_id: int
    username: str | None
    phone: str

    @field_validator("phone")
    @classmethod
    def validate_phone(cls, value: str) -> str:
        if validate_phone(phone=value):
            raise ValueError("Invalid phone format")
        return value
