from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Default App"
    env: str = "production"

    class Config:
        env_file = ".env"


settings = Settings()
