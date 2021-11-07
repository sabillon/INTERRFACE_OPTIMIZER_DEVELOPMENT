Copìar el documento adjunto en una carpeta y NO MODIFICARLE EL NOMBRE.

Abrir un Powershell como ADMINISTRADOR, con el comando cd ir a la carpeta donde se ha dejado el documento. Correr comando : docker-compose up
Si se cierra el power shell puede que se cierre el docker

Copiar archivos des del pc al docker
Abrir otro Power shell como administrador, ir con cd hasta el directorio que contiene la carpeta o archivo a enviar y usar el comando: docker cp .\NombreArchivoOCarpeta  (IDcontainer):home
La id del container se obtiene con el comando: docker ps

Para entrar en el bash para ejecutar cossas
Power shell como administrado, comando:  docker exec -it (IDContainer)  /bin/bash

Local host Insomnia:
GET http://127.0.0.1:5000/Optimitzation_ERMS