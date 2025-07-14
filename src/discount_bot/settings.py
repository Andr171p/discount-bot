from pathlib import Path
from dotenv import load_dotenv

from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent.parent.parent

ENV_PATH = BASE_DIR / ".env"

load_dotenv(ENV_PATH)


class BotSettings(BaseSettings):
    token: str = ""

    model_config = SettingsConfigDict(env_prefix="BOT_")


class PostgresSettings(BaseSettings):
    host: str = "postgres"
    port: int = 5432
    user: str = "postgres"
    password: str = "password"
    db: str = "discount"
    driver: str = "asyncpg"

    model_config = SettingsConfigDict(env_prefix="POSTGRES_")

    @property
    def url(self) -> str:
        return f"postgresql+{self.driver}://{self.user}:{self.password}@{self.host}:{self.port}/{self.db}"


class RabbitSettings(BaseSettings):
    host: str = "localhost"
    port: int = 5672
    user: str = "user"
    password: str = "password"

    model_config = SettingsConfigDict(env_prefix="RABBIT_")

    @property
    def url(self) -> str:
        return f"amqp://{self.user}:{self.password}@{self.host}:{self.port}"


class APISettings(BaseSettings):
    url: str = "https://example.com"

    model_config = SettingsConfigDict(env_prefix="API_")


class Settings(BaseSettings):
    bot: BotSettings = BotSettings()
    postgres: PostgresSettings = PostgresSettings()
    rabbit: RabbitSettings = RabbitSettings()
    api: APISettings = APISettings()
