from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Productivity Platform API"
    database_url: str = "sqlite:///./app.db"

    class Config:
        env_file = ".env"


settings = Settings()
