from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from fastapi_candidatos.database.engine import get_db
from fastapi_candidatos.schemas.candidato import CandidatoResponse, CandidatoCreate
from fastapi_candidatos.services.candidatos import crear_candidato

router = APIRouter(prefix="/candidato", tags=["Candidatos"])


@router.post("/", response_model=CandidatoResponse)
def add_candidato(candidato: CandidatoCreate, db: Session = Depends(get_db)):
    """
    Crea un nuevo candidato en la base de datos.

    Este endpoint recibe los datos de un candidato (DNI, nombre y apellido),
    los valida con el esquema `CandidatoCreate`, y los inserta en la base de datos.
    Devuelve el candidato creado, incluyendo el `id` generado automáticamente.

    Parameters
    ----------
    candidato : CandidatoCreate
        Objeto con los datos del candidato enviados en la petición.
    db : Session, optional
        Sesión activa de la base de datos inyectada como dependencia.

    Returns
    -------
    CandidatoResponse
        Objeto con los datos del candidato recién creado.

    """
    return crear_candidato(db, candidato)
