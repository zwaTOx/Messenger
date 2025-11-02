from pydantic_settings import BaseSettings, SettingsConfigDict

class AuthTokenSettings(BaseSettings):
    JWT_EXP_MIN: int
    JWT_ALG: str
    JWT_SECRET_KEY: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore"
    )

auth_token_settings = AuthTokenSettings()