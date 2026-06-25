from pydantic import BaseModel


class Settings(BaseModel):
    app_name: str = "NAMI"
    version: str = "0.1.0"
    debug: bool = True


settings = Settings()
