from enum import Enum
from pathlib import Path
from typing import Self

from pydantic import HttpUrl, DirectoryPath, BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class Browser(str, Enum):
    WEBKIT = "webkit"
    FIREFOX = "firefox"
    CHROMIUM = "chromium"


class TestUser(BaseModel):
    username: str
    password: str


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_nested_delimiter=".",
        extra="allow"

    )

    app_url: HttpUrl
    headless: bool
    browsers: list[Browser]
    test_user: TestUser
    videos_dir: DirectoryPath
    tracing_dir: DirectoryPath
    allure_results_dir: DirectoryPath

    @classmethod
    def initialize(cls) -> Self:
        for path in [
            Path("videos"),
            Path("tracing"),
            Path("allure-results"),
        ]:
            path.mkdir(exist_ok=True)

        return cls()


settings = Settings.initialize()
