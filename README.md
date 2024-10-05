Gestor de Tareas en Flask

Este es un proyecto simple de gestión de tareas utilizando Flask y SQLite. Sigue los pasos a continuación para instalar y ejecutar el proyecto en tu máquina local.
Requisitos previos

Antes de comenzar, asegúrate de tener instalado lo siguiente:

  Python 3.8 o superior: Puedes descargar Python desde su pagina oficial : https://www.python.org/

Paso 1: Clonar el repositorio
 
 Abre la terminal (o Git Bash en Windows).
 Navega hasta el directorio donde deseas clonar el proyecto.
 Clona el repositorio utilizando el siguiente comando:


    git clone https://github.com/JacoboCerritos/Gestion-de-tareas.git

Entra en la carpeta del proyecto:


    cd Gestion_tareas


Paso 2: Crear y activar un entorno virtual (opcional pero recomendado)

Crear un entorno virtual te ayuda a mantener las dependencias del proyecto aisladas.

  Crea el entorno virtual:


    python -m venv venv

Activa el entorno virtual:

Windows:


    venv\Scripts\activate

Linux/macOS:


    source venv/bin/activate


Paso 3: Instalar dependencias

  Asegúrate de estar en el directorio del proyecto y con el entorno virtual activado (si lo creaste).

  Instala las dependencias necesarias que están en el archivo requirements.txt:


    pip install -r requirements.txt


Paso 4: Crear la base de datos

  Ejecuta el archivo create_db.py para crear la base de datos SQLite:

  
    python create_db.py

Esto creará un archivo llamado tasks.db en el directorio del proyecto con la tabla necesaria para almacenar las tareas.


Paso 5: Ejecutar el servidor

  Inicia la aplicación Flask:


    python app.py


La aplicación estará corriendo en http://127.0.0.1:5000/. Abre esa dirección en tu navegador para acceder a la aplicación.



Paso 6: Uso de la aplicación

  Una vez que la aplicación esté ejecutándose:

  Puedes agregar tareas utilizando el formulario en la página principal.
  Puedes marcar tareas como completadas o eliminarlas.

Problemas comunes

  Error 404: Asegúrate de que el servidor Flask esté corriendo.
  
  No aparece la base de datos: Si la base de datos no se crea correctamente, asegúrate de ejecutar create_db.py antes de iniciar la aplicación.
