# APIConsumer

Creación e implementación de una API que consume servicios financieros y extrae datos por medio de APIS WEB proporcionadas por tres proveedores:
* [DOF](https://www.banxico.org.mx/tipcamb/tipCamMIAction.do)
* [Fixerio](https://fixer.io/)
* [Banxico](https://www.banxico.org.mx/SieAPIRest/service/v1/doc/consultaDatosSerieRango)

![Listado de funciones](https://github.com/vicogarcia16/APIConsumer/blob/master/capturas/captura1.JPG)

## Instalación 🔧

* Descargar y clonar el repositorio
* Crear un entorno virtual para Python si se desea trabajar en local y ejecutar el archivo requirements.txt
* Si se requiere ejecutar en Docker, favor de realizar el siguiente comando: docker-compose up -d 

## Ejecución del software ⚙️
### Local
* Ejecutar el comando en cmd o terminal [uvicorn main:app --reload]
* Posteriormente acceder a la url por defecto [127.0.0.1:8000]
### Docker
* Si ha realizado la imagen Docker ejecutar el contenedor creado "micro-service-fastapi" y posteriormente abrir el navegador en la URL: [localhost:8000]
### Autenticación
* Para tener autorización sobre los elementos o petiiciones GET, registrar un usuario y contraseña temporal o en su defecto loggearse. Esto se realiza, 
para recibir el token de acceso (Nota: Dicho token caduca a los 10 minutos)

![Ingresar usuario](https://github.com/vicogarcia16/APIConsumer/blob/master/capturas/captura2.JPG)
* Dar clic al botón [Authorize] y pegar el token en el input de tipo texto

![Ingresar token](https://github.com/vicogarcia16/APIConsumer/blob/master/capturas/captura3.JPG)
### Peticiones GET
* Recuerde que cada proveedor requiere su propio API de acceso. En el caso de DOF no lo requiere, sin embargo en el caso de Banxico y Fixerio si se requiere.
* Se realizaron salidas de información para cada uno de los proveedores como se observa en la primera imagen y una petición GET llamada "Datos" la cual 
recibe la información de los tres proveedores como se observa en la siguiente imagen.

![Ingresar token](https://github.com/vicogarcia16/APIConsumer/blob/master/capturas/captura4.JPG)
## Construido con 🛠️

* [Python](https://www.python.org/) - Lenguaje de programación
* [FastAPI](https://fastapi.tiangolo.com/) - Framework Web
* [JWT](https://jwt.io/) - Verificación de acceso con tokens

## Autor ✒️

* **Víctor García** [vicogarcia16](https://github.com/vicogarcia16) 
