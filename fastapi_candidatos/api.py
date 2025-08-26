from fastapi import FastAPI, APIRouter
from fastapi_candidatos.routers import candidatos

# -------------------------------------------------
# Inicialización de la aplicación FastAPI
# -------------------------------------------------
app = FastAPI(
    title="API Candidatos",
    version="1.0.0",
    docs_url="/api/docs",
    description=(
        "API para la gestión de candidatos. Permite crear y consultar "
        "registros de candidatos con sus datos principales."
    ),
)


# -------------------------------------------------
# Router principal de la API
# -------------------------------------------------
api_router = APIRouter(prefix="/api/v1")

# Incluir subrouters
api_router.include_router(candidatos.router, prefix="/candidatos", tags=["Candidatos"])

# -------------------------------------------------
# Incluir router en la aplicación principal
# -------------------------------------------------
app.include_router(api_router)
