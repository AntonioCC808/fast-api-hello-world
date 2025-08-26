import os
from pydantic import BaseSettings
from dotenv import load_dotenv

# Cargar variables desde archivo .env si existe
load_dotenv()

class Settings(BaseSettings):
    """
    Configuración general de la aplicación.
    Prioriza DATABASE_URL desde entorno o .env,
    y si no existe, usa SQLite por defecto.
    """
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL",
        "sqlite:///./candidatos.db"  # fallback si no hay variable definida
    )

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
