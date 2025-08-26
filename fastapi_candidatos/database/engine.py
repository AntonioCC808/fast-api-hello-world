from contextlib import contextmanager
from typing import Any, Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from fastapi_candidatos.config import settings

# Create SQLAlchemy engine
engine = create_engine(settings.DATABASE_URL)

# Session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Generator[Session, Any, None]:
    """
    Dependencia que proporciona una sesión de base de datos con SQLAlchemy.

    Esta función se utiliza como dependencia en FastAPI para inyectar
    una sesión de base de datos en los endpoints. La sesión se cierra
    automáticamente al finalizar la petición.

    Yields
    ------
    Session
        Sesión activa de SQLAlchemy para interactuar con la base de datos.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@contextmanager
def get_db_context():
    """
    Proporciona una sesión de base de datos mediante un gestor de contexto.

    Esta función permite trabajar con la base de datos en bloques `with`,
    asegurando que la sesión se cierre correctamente al finalizar.

    Yields
    ------
    Session
        Sesión activa de SQLAlchemy dentro de un bloque `with`.

    """
    db_gen = get_db()
    db = next(db_gen)
    try:
        yield db
    finally:
        try:
            next(db_gen)  # Cierra la sesión
        except StopIteration:
            pass