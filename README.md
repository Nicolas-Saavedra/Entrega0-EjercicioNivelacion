# Entrega Ejercicio Nivelacion

Este es el repositorio que contiene el codigo para la entrega del ejercicio
de nivelacion de la materia de ISIS4XXX de Cloud. Esta applicacion esta
compuesta de tres componentes principales: El front que se encuentra escrito
en SvelteKit y es renderizado por Caddy, el back que fue escrito en FastAPI
y corre en uvicorn, y una base de datos PostgreSQL, corriendo en un contenedor
con volumen para mantener persistencia.

## Rutas principales

- `/api/v1/docs`: Ruta para probar los endpoints por medio de FastAPI y OpenAPI,
donde se pueden probar las rutas con o sin autenticacion y los modelos usados

- `/login`: Pagina de login, redireccionamiento automatico si se detecta que no
se encuentra loggeado el usuario actual

- `/tasks`: Pagina para crear, editar, y eliminar tareas del usuario actual. Se
pueden observar las tareas proximas, junto con su classificacion

- `/tasks/categories`: Pagina para crear y eliminar categorias del usuario actual.
Se pueden observar las categorias, sus descripciones, y si son eliminadas, las
tareas asociadas tambien son eliminadas

## Instalacion y uso

Para instalar/usar esta applicacion, se utilizara la herramienta `docker-compose`,
la cual permite declarar la configuracion de los contenedores de manera declarativa,
con el fin de poder recrear la estructura deseada para el deployment, ya sean
volumenes, redes y/o hostnames, contenedores, variables de entorno, etc.

1. Clonar este repositorio en la maquina virtual en la que se desea correr
    el proyecto

    ```sh
    git clone https://github.com/Nicolas-Saavedra/Entrega0-EjercicioNivelacion.git
    ```

2. Cree los archivos `.env.deployment` en las carpetas `frontend`, `backend` y
    `postgres`. Estas contendran las variables de entorno para poder correr las tres
    applicaciones. A continuacion, se muestran ejemplos de variables de entoro posibles
    para estas applicaciones:

    `frontend/.env.production`

    ```env
    PUBLIC_API_URL=http://localhost/api/v1
    ```

    `backend/.env.production`

    ```env
    JWT_SECRET_KEY=655ca1e37dc2b65b1cfd784ceb8914621c8658db33252e9077b9e208cd597bd2
    JWT_REFRESH_SECRET_KEY=0a81f4555f3b27b7c1ff3b632b3ff86935104a721be0a5871df8ba5304a565fd
    DATABASE_URL=postgresql://postgres:<password>@postgres.local/postgres
    ```

    Tip: Se puede usar `openssl rand -base64 32` en la terminal para crear una llave
    como las que se observan en el ejemplo

    `postgres/.env.production`

    ```env
    POSTGRES_PASSWORD=<password>
    ```

3. Despues de creados los archivos, correr el docker compose:

    ```sh
    sudo docker compose up -d
    ```

    Tip: Si se esta usando `root` o un usuario en el grupo de `docker`,
    se puede evitar usar `sudo`.

## Creditos

- Nicolas Saavedra Gonzalez
- Nicolas Saavedra Gonzalez
- Nicolas Saavedra Gonzalez
- Nicolas Saavedra Gonzalez
- Nicolas Saavedra Gonzalez
