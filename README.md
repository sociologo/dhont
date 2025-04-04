# dhont

![image](https://github.com/user-attachments/assets/97367d9c-902a-40c6-8163-b7e1711a407a)

1 Creamos la carpeta `C:\mis_entornos\entorno_4`:

2 Creamos el entorno:

```
C:\>cd mis_entornos
C:\mis_entornos> python -m venv entorno_4
C:\mis_entornos> cd entorno_4/Scripts
C:\mis_entornos\entorno_4\Scripts> activate
(entorno_4) C:\mis_entornos\entorno_4\Scripts>
(entorno_4) C:\mis_entornos\entorno_4\Scripts> cd /
(entorno_4) C:\>
```

3 Instalamos las dependencias en tal entorno:

```
C:\>cd mis_entornos/entorno_4/Scripts
C:\mis_entornos\entorno_4\Scripts> activate
(entorno_4) C:\mis_entornos\entorno_4\Scripts> pip install django
(entorno_4) C:\mis_entornos\entorno_4\Scripts> python.exe -m pip install --upgrade pip
(entorno_4) C:\mis_entornos\entorno_4\Scripts> pip install django-ckeditor
(entorno_4) C:\mis_entornos\entorno_4\Scripts> pip install psycopg2-binary
(entorno_4) C:\mis_entornos\entorno_4\Scripts> pip install Pillow
```

4 Construímos la aplicación:

```
C:\> cd mis_entornos/entorno_4/Scripts
C:\mis_entornos\entorno_4\Scripts> activate
(entorno_4) C:\mis_entornos\entorno_4\Scripts> cd \mis_proyectos
(entorno_4) C:\mis_proyectos> django-admin startproject dhont
```

y se crea la carpeta contenedora `dhont` en la carpeta `mis_proyectos`

5 Verificamos:

```
(entorno_4) C:\mis_proyectos>  cd dhont
(entorno_4) C:\mis_proyectos\dhont>python manage.py runserver
```

6 Creamos la carpeta `applications` a la altura de manage.py

![image](https://github.com/user-attachments/assets/6845ddc3-aae6-4593-a33e-0834d1d7665a)

![image](https://github.com/user-attachments/assets/04977199-7a94-4335-b3e0-07ad73bfd827)

7 Creamos la carpeta settings con su cuatro archivos interiores y borramos el settings original

![image](https://github.com/user-attachments/assets/a6303270-a68e-470a-9cfa-c4cbf7cdc77d)

8 Le indicamos a django que ejecute desde el entorno de configuración local.py:

9 Verificamos:

(entorno_4) C:\mis_proyectos\dhont> python manage.py runserver

9 Vamos al nivel de applications y creamos 4 nuevos proyectos:

(entorno_4) C:\mis_proyectos\dhont>cd applications
(entorno_4) C:\mis_proyectos\dhont\applications> django-admin startapp partidos
(entorno_4) C:\mis_proyectos\dhont\applications> django-admin startapp escanos
(entorno_4) C:\mis_proyectos\dhont\applications> django-admin startapp elecciones
(entorno_4) C:\mis_proyectos\dhont\applications> django-admin startapp votos

10  Ahora necesitamos instalar nuestras aplicaciones en el archivo base.py:

INSTALLED_APPS = [
   'django.contrib.admin',
   'django.contrib.auth',
   'django.contrib.contenttypes',
   'django.contrib.sessions',
   'django.contrib.messages',
   'django.contrib.staticfiles',

   'applications.partidos',
   'applications.escanos',
   'applications.elecciones',
   'applications.votos'
]

11 En cada uno de los archivos apps.py de las aplicaciones anteponemos el prefijo `applications.`:

Verificamos:

(entorno_4) C:\mis_proyectos\dhont> python manage.py runserver


















