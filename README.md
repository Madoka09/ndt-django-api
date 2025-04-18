# Prueba Tecnica para NTD Software

Este proyecto es una pequeña API RESTful construida con Django y Django REST Framework. Permite gestionar información de planetas (crear, leer, actualizar, eliminar) y cuenta con un endpoint para cargar una tanda inicial de datos desde un endpoint de una API de GraphQL

## Requisitos

- Python 3.12+ (El venv inicial fue creado con python 3.12 como base)
- pip

## Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tu_usuario/planet-api.git
   cd planet-api
   ```

2. Crea y activa un entorno virtual:
   ```bash
   python -m venv env
   source env/bin/activate  # en Windows: env\Scripts\activate
   ```

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Aplica las migraciones:
   ```bash
   python manage.py migrate
   ```

## Ejecución del servidor

Inicia el servidor de desarrollo de Django con:

```bash
python manage.py runserver
```

La url del servidor suele ser la siguiente:
`http://127.0.0.1:8000/`

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