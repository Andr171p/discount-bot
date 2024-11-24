from pydantic import BaseModel, field_validator

from src.utils import validate_phone


class UserSchema(BaseModel):
    user_id: int
    username: str
    phone: str

    @field_validator("phone")
    @classmethod
    def validate_phone(cls, v: str) -> str:
        if validate_phone(phone=v):
            raise ValueError("Invalid phone format")
        return v
