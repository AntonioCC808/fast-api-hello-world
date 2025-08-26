# Imagen base con micromamba
FROM mambaorg/micromamba:1.5.8

# Definir directorio de trabajo
WORKDIR /app

# Copiar environment.yml
COPY environment.yml .

# Instalar dependencias en el entorno base
RUN micromamba install -n base -f environment.yml -y && \
    micromamba clean --all --yes

# Copiar el código de la aplicación
COPY . .

# Exponer puerto de la API
EXPOSE 8000

# Ejecutar directamente el main.py
CMD ["micromamba", "run", "-n", "base", "python", "fastapi_candidatos.main.py"]

