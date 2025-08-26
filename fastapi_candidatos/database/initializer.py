from fastapi_candidatos.database.engine import engine
from fastapi_candidatos.database.orm_models import Base
from fastapi_candidatos.database import orm_models


def init_db() -> None:
    """
    Inicializa la base de datos creando las tablas definidas en los modelos ORM.

    Esta función se encarga de invocar a `Base.metadata.create_all` sobre
    el motor configurado en `engine`. Si las tablas no existen, se crean
    automáticamente en la base de datos configurada (SQLite, MySQL, etc.).

    Notes
    -----
    - No elimina ni modifica tablas existentes, solo crea las que falten.
    - Se recomienda ejecutar esta función al inicio de la aplicación
      para asegurar que la base de datos está lista.

    Examples
    --------
    """
    Base.metadata.create_all(bind=engine)
