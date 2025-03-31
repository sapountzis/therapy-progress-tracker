from typing import Annotated

from pydantic import field_validator
from pydantic_settings import BaseSettings, NoDecode


class Settings(BaseSettings):
    DATABASE_URL: str
    LANGFUSE_HOST: str
    LANGFUSE_PUBLIC_KEY: str
    LANGFUSE_SECRET_KEY: str
    OPENAI_API_KEY: str
    THERAPY_METRICS: Annotated[list[str], NoDecode]

    class Config:
        env_file = "progress_tracker.env"

    @field_validator("THERAPY_METRICS", mode="before")
    @classmethod
    def decode_numbers(cls, v: str) -> list[str]:
        return v.split(",")


def get_settings() -> Settings:
    return Settings()
