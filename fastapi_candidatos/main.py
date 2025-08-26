"""
Punto de entrada principal del backend.

Este script:
1. Carga las variables de entorno desde `.env`.
2. Inicializa la base de datos creando las tablas necesarias.
3. Inicia la aplicación FastAPI con Uvicorn.
"""

import uvicorn
import dotenv

from fastapi_candidatos.database.initializer import init_db

if __name__ == "__main__":
    # Cargar variables de entorno desde .env
    dotenv.load_dotenv()

    # Inicializar base de datos
    init_db()

    # Ejecutar aplicación con Uvicorn
    uvicorn.run(
        "fastapi_candidatos.api:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
