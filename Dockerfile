# Usar una imagen base de Python
FROM python:3.9-slim
# Se establece una variable de entorno para que se ejecute en modo sin buffer
ENV PYTHONUNBUFFERED=1

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Copiar los archivos de requisitos al contenedor
COPY requirements.txt .

# Instalar las dependencias necesarias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código de la aplicación al contenedor
COPY . .

# Exponer el puerto en el que correrá la API (UVICORN USA 8000 POR DEFECTO)
EXPOSE 8000

# Comando para correr la aplicación usando Uvicorn
CMD ["uvicorn", "app:app", "--host", "--port", "8000"]
