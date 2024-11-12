from typing import ClassVar

from pydantic_settings import SettingsConfigDict

from src.project.settings.database import PostgreSQLSettings


class Settings(PostgreSQLSettings):
    model_config: ClassVar[SettingsConfigDict] = SettingsConfigDict(
        case_sensitive=False,
        env_file=".env",
        extra="ignore",
    )
