from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    database_url: str = ""
    jwt_secret_key: str = ""
    jwt_refresh_secret_key: str = ""

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()
