# Imagen base de python 
FROM python:3.8.1-slim-buster

# Directorio de trabajo
WORKDIR /usr/src/app

# Indica al inteprete de Python que no genere archivos .pyc
ENV PYTHONDONTWRITEBYTECODE 1

# Indica a Python que su salida estandar se envie directamente 
# a la terminal, sin esperar en un buffer intermedio.
ENV PYTHONUNBUFFERED 1

# Indica a Flask, que es lo que debe ejecutar primero
ENV FLASK_APP=app/app.py

# Instalar dependencias
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

# Copiar archivos de proyecto al directorio de trabajo
COPY . /usr/src/app/

# Indica a Flask que levante un servidor
# 0.0.0.0 : El servidor sera publicamente visible
# ${PORT:-5000} : El puerto donde se bindea el server 
# esta especificado por la variable de entorno PORT.  
# PORT=5000, por defecto.
CMD flask run --host=0.0.0.0 --port=${PORT:-5000}