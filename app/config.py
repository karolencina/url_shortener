# importing pydantic - you install pydantic automatically when you install fastapi with pip.
from pydantic import BaseSettings
# The lru_cache decorator allows you to cache the result of get_settings() using the LRU strategy
from functools import lru_cache 

# The Settings class is a subclass of BaseSettings
class Settings(BaseSettings):
    # Default value for Name of your current environment
    env_name: str = "Local"
    # Default value for Domain of your app
    base_url: str = "http://localhost:8000"
    # Default value for Address of your database
    db_url: str = "sqlite:///./shortener.db"

    class Config:
        env_file = ".env"

@lru_cache
def get_settings() -> Settings:
    settings = Settings()
    print(f"Loading settings for: {settings.env_name}")
    # function returns an instance of your Settings class and will provide you with the option of caching your settings
    return settings
