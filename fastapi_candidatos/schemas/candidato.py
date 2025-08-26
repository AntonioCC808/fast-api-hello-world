from pydantic import BaseModel

class CandidatoBase(BaseModel):
    dni: str
    nombre: str
    apellido: str

class CandidatoCreate(CandidatoBase):
    pass

class CandidatoResponse(CandidatoBase):
    id: int

    class Config:
        orm_mode = True
