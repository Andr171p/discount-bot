import os
from pathlib import Path
from dotenv import load_dotenv
from pydantic_settings import BaseSettings


BASE_DIR: Path = Path(__file__).resolve().parent.parent

ENV_PATH: Path = BASE_DIR / ".env"

load_dotenv(dotenv_path=ENV_PATH)


class SQLiteConfig(BaseSettings):
    url: str = f"sqlite+aiosqlite:///{BASE_DIR}/src/database/data/users.db"


class PostgreSQLConfig(BaseSettings):
    user: str = os.getenv("DB_USER")
    password: str = os.getenv("DB_PASSWORD")
    host: str = os.getenv("DB_HOST")
    port: int = os.getenv("DB_PORT")
    url: str = f"postgresql+asyncpg://{user}:{password}@{host}:{port}/railway"


class MessagesConfig(BaseSettings):
    start: Path = BASE_DIR / "src" / "static" / "messages" / "start.json"
    auth: Path = BASE_DIR / "src" / "static" / "messages" / "auth.json"


class TelegramConfig(BaseSettings):
    token: str = os.getenv("BOT_TOKEN")


class Config(BaseSettings):
    telegram: TelegramConfig = TelegramConfig()
    sqlite: SQLiteConfig = SQLiteConfig()
    postgresql: PostgreSQLConfig = PostgreSQLConfig()
    messages: MessagesConfig = MessagesConfig()


config = Config()
