# Usar imagen base de Python
FROM python:3.11-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar el archivo requirements.txt e instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código de la aplicación
COPY app.py .

# Establecer la variable de entorno para el puerto
ENV PORT=5000

# Exponer el puerto de la aplicación
EXPOSE 5000

# Crear un usuario no-root y usarlo
RUN useradd -m appuser
USER appuser

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]