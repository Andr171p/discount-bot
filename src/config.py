import os
from pathlib import Path
from dotenv import load_dotenv
from pydantic_settings import BaseSettings
from typing import Dict


BASE_DIR: Path = Path(__file__).resolve().parent.parent

ENV_PATH: Path = BASE_DIR / ".env"

load_dotenv(dotenv_path=ENV_PATH)


class DBConfig(BaseSettings):
    ...


class TelegramConfig(BaseSettings):
    token: str = os.getenv("TELEGRAM_TOKEN")


class APIConfig(BaseSettings):
    url: str = os.getenv("API_URL")
    token: str = os.getenv("API_TOKEN")
    headers: Dict[str, str] = {'Content-Type': 'application/json; charset=UTF-8'}
    order: str = "status"
    orders: str = "statuses"
    flyer: str = "bonus"
    history: str = "history"


class Config(BaseSettings):
    telegram: TelegramConfig = TelegramConfig()
    api: APIConfig = APIConfig()


config = Config()
