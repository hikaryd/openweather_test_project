from pydantic import BaseSettings


class Settings(BaseSettings):
    app_title: str = "TestProjectOpenWeather"
    database_url: str = "sqlite+aiosqlite:///./fastapi.db"
    secret: str = "secret"
    openweathermap_key: str = "d6f93bf44c7ae06b56225112ee80901d"

    class Config:
        env_file = ".env"


settings = Settings()
