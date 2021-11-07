FROM python:3 
# importar imagen base

WORKDIR python 
# Crear un directorio en el docker

COPY . /python 
# copiar en la carpeta actual del ordenador en la carpeta python del docker

RUN ls

EXPOSE 5000

RUN pip install --no-cache-dir -r ./requirements.txt
#instala librerias descritas en el .txt

CMD ["python", "-u","./app.py"] 
