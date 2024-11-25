import os
from pathlib import Path
from dotenv import load_dotenv
from pydantic_settings import BaseSettings
from typing import Dict


BASE_DIR: Path = Path(__file__).resolve().parent.parent

ENV_PATH: Path = BASE_DIR / ".env"

load_dotenv(dotenv_path=ENV_PATH)


class DBConfig(BaseSettings):
    url: str = f"sqlite+aiosqlite:///{BASE_DIR}/src/database/data/users.db"


class StorageConfig(BaseSettings):
    host: str = "localhost"
    port: int = 6379
    db: int = 0
    expire_timeout: int = 86400


class MessagesConfig(BaseSettings):
    start: Path = BASE_DIR / "src" / "static" / "messages" / "start.json"
    auth: Path = BASE_DIR / "src" / "static" / "messages" / "auth.json"


class TelegramConfig(BaseSettings):
    token: str = os.getenv("BOT_TOKEN")


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
    db: DBConfig = DBConfig()
    storage: StorageConfig = StorageConfig()
    messages: MessagesConfig = MessagesConfig()


config = Config()
