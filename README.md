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

12 Implementando la base de datos



```python
from django.db import models
from datetime import date

class Elecciones(models.Model):
   nombre = models.CharField("Nombre", max_length=50)
   fecha = models.DateField("Fecha", default=date.today)

   def __str__(self):
      return str(self.id) + "-" + self.date
```
```python
from django.db import models

class Partidos(models.Model):
   nombre = models.CharField("Nombre", max_length=50)
   siglas = models.CharField("Nombre", max_length=50)

   def __str__(self):
      return str(self.id) + "-" + self.nombre + "-" + self.siglas
```
```python
from django.db import models
from applications.elecciones.models import Elecciones
from applications.partidos.models import Partidos

class Escanos(models.Model):
   escanos = models.IntegerField()
   eleccion = models.ForeignKey(Elecciones, on_delete=models.CASCADE)
   partido = models.ForeignKey(Partidos, on_delete=models.CASCADE)

   def __str__(self):
      return str(self.id) + "-" + self.name
```
```python
from django.db import models
from applications.elecciones.models import Elecciones
from applications.partidos.models import Partidos

class Votos(models.Model):
   votos = models.IntegerField()
   eleccion = models.ForeignKey(Elecciones, on_delete=models.CASCADE)
   partido = models.ForeignKey(Partidos, on_delete=models.CASCADE)

   def __str__(self):
      return str(self.id) + "-" + self.name
```



```bash
(entorno_4) C:\mis_proyectos\dhont>python manage.py makemigrations
Migrations for 'elecciones':
  applications\elecciones\migrations\0001_initial.py
    + Create model Elecciones
Migrations for 'partidos':
  applications\partidos\migrations\0001_initial.py
    + Create model Partidos
Migrations for 'votos':
  applications\votos\migrations\0001_initial.py
    + Create model Votos
Migrations for 'escanos':
  applications\escanos\migrations\0001_initial.py
    + Create model Escanos

(entorno_4) C:\mis_proyectos\dhont>python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, elecciones, escanos, partidos, sessions, votos
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying elecciones.0001_initial... OK
  Applying partidos.0001_initial... OK
  Applying escanos.0001_initial... OK
  Applying sessions.0001_initial... OK
  Applying votos.0001_initial... OK

(entorno_4) C:\mis_proyectos\dhont>
```

Registramos en el admin.py de las apps las tablas recién construídas.

```python
from django.contrib import admin # type: ignore
from .models import Elecciones
admin.site.register(Elecciones)
```
```python
from django.contrib import admin # type: ignore
from .models import Partidos
admin.site.register(Partidos)
```
```python
from django.contrib import admin # type: ignore
from .models import Escanos
admin.site.register(Escanos)
```
```python
from django.contrib import admin # type: ignore
from .models import Votos
admin.site.register(Votos)
```

 Creamos un superuser:

```python
(entorno_4) C:\mis_proyectos\dhont>python manage.py createsuperuser
Username (leave blank to use 'chris'):
Email address: tarredwall@gmail.com
Password:
Password (again):
This password is too short. It must contain at least 8 characters.
This password is too common.
This password is entirely numeric.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
```
La clave es: 123456











