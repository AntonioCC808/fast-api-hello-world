from sqlalchemy.orm import Session

from fastapi_candidatos.database import orm_models
from fastapi_candidatos.schemas.candidato import CandidatoCreate


def crear_candidato(db: Session, candidato: CandidatoCreate):
    """
    Crea un nuevo candidato en la base de datos.

    Inserta un registro en la tabla `candidatos` a partir de los datos
    proporcionados en el esquema `CandidatoCreate`.

    Parameters
    ----------
    db : Session
        Sesión activa de la base de datos (SQLAlchemy).
    candidato : CandidatoCreate
        Objeto con los datos del candidato (dni, nombre, apellido).

    Returns
    -------
    orm_models.Candidato
        Objeto del candidato recién creado en la base de datos,
        incluyendo el `id` generado automáticamente.

    """
    db_candidato = orm_models.Candidato(**candidato.dict())
    db.add(db_candidato)
    db.commit()
    db.refresh(db_candidato)
    return db_candidato
