# Prueba Tecnica para NTD Software

Este proyecto es una pequeña API RESTful construida con Django y Django REST Framework. Permite gestionar información de planetas (crear, leer, actualizar, eliminar) y cuenta con un endpoint para cargar una tanda inicial de datos desde un endpoint de una API de GraphQL

## Requisitos

- Docker
- Docker Compose

## Soporte para Docker y Docker Compose

Se agregó soporte básico para Docker y Dokcer Compose con el fin de intentar emular un entorno parecido al de producción.

> Nota: No tengo experiencia profesional usando Docker, sin embargo he ejecutado y creado contenedores para proyectos personales previamente.

## Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/Madoka09/ntd-django-api.git
   cd ntd-django-api
   ```

2. Ejecutar docker compose:
   ```bash
   docker compose up --build
   ```

3. En otra terminal ejecutar las migraciones:
   ```bash
   docker compose exec web python manage.py migrate
   ```

4. Para probar la API, se puede ingresar a la URL:
   ```bash
   http://localhost:8000
   ```

5. Para detener el contenedor y limpiar se puede usar el comando:
   ```bash
   docker compose down
   ```

## Cambios respecto a la versión anterior:

1. Se usa PostrgreSQL en lugar de sqlite como el motor de base de datos.
2. Ahora se usa Poetry como gestor de dependencias y entorno.
3. Ya no es necesario instalar dependencias o crear un entorno virtual
4. Se complementó el serializador del modelo Planet con validaciones sencillas.

## Endpoints

### CRUD

Estos son los metodos disponibles usando el Django rest framework:
                   
>GET     `/planets/`            Listar todos los planetas            
>POST    `/planets/`            Crear un nuevo planeta               
>GET     `/planets/<id>/`       Obtener detalles de un planeta       
>PATCH   `/planets/<id>/`       Editar parcialmente un planeta       
>PUT     `/planets/<id>/`       Editar completamente un planeta      
>DELETE  `/planets/<id>/`       Eliminar un planeta                  

### Realizar la carga inicial de datos

Este endpoint carga datos de planetas desde el endpoint proporcionado para la prueba: https://swapi-graphql.netlify.app/.netlify/functions/index?query=query%20Query%20%7BallPlanets%7Bplanets%7Bname%20population%20terrains%20climates%7D%7D%7D, **pero solo puede ejecutarse una vez**.

>GET    `/load-data/load/`            Carga los planetas iniciales (una vez)

Una vez que se ha hecho la carga inicial el endpoint retornará el codigo de estado 403, si hay 
al menos un registro en la base de datos, esto está hecho con el proposito de no sobreescribir la base de datos.