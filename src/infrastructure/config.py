from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    LOG_LEVEL: str = 'INFO'
    ENVIRONMENT: str = 'development'

    class Config:
        env_file = '.env'


settings = Settings()
