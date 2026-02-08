import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Agri-Drishti"
    
    # Database (Defaults match docker-compose)
    POSTGRES_USER: str = os.getenv("POSTGRES_USER", "admin")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD", "secure_password")
    POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER", "db")
    POSTGRES_DB: str = os.getenv("POSTGRES_DB", "agri_drishti")
    
    # Construct Database URL
    DATABASE_URL: str = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}/{POSTGRES_DB}"

    # Google Earth Engine Key Path
    # This must match where we mounted it in docker-compose.yml
    EE_KEY_PATH: str = "/app/credentials/ee-key.json"

# 🚨 THIS IS THE LINE YOU WERE MISSING 🚨
settings = Settings()