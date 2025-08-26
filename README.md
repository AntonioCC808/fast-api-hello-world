# 🚀 FastAPI Candidatos

API de gestión de candidatos construida con **FastAPI**, **SQLAlchemy** y **Pydantic**.

---

## ⚙️ Requisitos previos
- Python 3.11 (si corres en local)
- [Docker](https://www.docker.com/) y [Docker Compose](https://docs.docker.com/compose/) (si usas contenedores)

---

## ▶️ 1. Ejecutar con Docker Compose (MySQL + API)

Este modo levanta dos servicios:
- **API** (FastAPI + Uvicorn)
- **MySQL** como base de datos

### 🔹 Pasos

1. Crea un archivo `.env` en la raíz del proyecto con la siguiente variable:

   ```ini
   DATABASE_URL=mysql+pymysql://user:password@db:3306/candidatos
   ```

2. Construye y levanta los contenedores:

   ```bash
   docker compose build --no-cache
   docker compose up -d
   ```

3. Comprueba que todo está corriendo:

   ```bash
   docker ps
   ```

4. Abre la documentación interactiva de la API en Swagger UI:  
   👉 [http://localhost:8080/api/docs](http://localhost:8080/api/docs)

### 🔹 Parar servicios

```bash
docker compose down
```

---

## ▶️ 2. Ejecutar en local con SQLite

Este modo usa una base de datos **SQLite** (`candidatos.db`) creada en la carpeta raíz.

### 🔹 Pasos

1. Crea un entorno e instala dependencias (ejemplo con mamba):

   ```bash
   mamba env create -f environment.yml
   mamba activate fastapi-candidatos
   ```

2. Crea un archivo `.env` (opcional, solo si quieres usar MySQL):

   ```ini
   # Si no está definido, por defecto se usará SQLite
   DATABASE_URL=sqlite:///./candidatos.db
   ```

3. Ejecuta el servidor FastAPI:

   ```bash
   python -m fastapi_candidatos.main
   ```

4. Accede a la API en:  
   👉 [http://127.0.0.1:8000/api/docs](http://127.0.0.1:8000/api/docs)

---

## 📂 Estructura del proyecto

```
fastapi_candidatos/
├── database/
│   ├── engine.py
│   ├── initializer.py
│   └── orm_models.py
├── routers/
│   └── candidatos.py
├── schemas/
│   └── candidato.py
├── services/
│   └── candidatos.py
├── config.py
├── main.py
docker-compose.yml
environment.yml
Dockerfile
```

---

## ✅ Endpoints principales

- `POST /api/v1/candidatos/` → Crear un candidato