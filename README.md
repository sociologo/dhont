# dhont

# Script de arranque:

```
C:\Users\chris> cd \
C:\> cd mis_entornos/entorno_4/Scripts
C:\mis_entornos\entorno_4\Scripts> activate
C:\mis_entornos\entorno_4\Scripts> cd \
C:\> cd \GitHub\dhont\dhont
C:\GitHub\dhont\dhont> python manage.py runserver
```

```
(entorno_4) C:\GitHub\dhont\dhont> git branch
  main
* rama-1
```

# La estructura básica del proyecto

![image](https://github.com/user-attachments/assets/97367d9c-902a-40c6-8163-b7e1711a407a)

1 Creamos la carpeta `C:\mis_entornos\entorno_4`:

2 Creamos el entorno:

```
C:\> cd mis_entornos
C:\mis_entornos> python -m venv entorno_4
C:\mis_entornos> cd entorno_4/Scripts
C:\mis_entornos\entorno_4\Scripts> activate
(entorno_4) C:\mis_entornos\entorno_4\Scripts>
(entorno_4) C:\mis_entornos\entorno_4\Scripts> cd /
(entorno_4) C:\>
```

3 Instalamos las dependencias en tal entorno:

```
C:\> cd mis_entornos/entorno_4/Scripts
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
(entorno_4) C:\mis_proyectos> cd dhont
(entorno_4) C:\mis_proyectos\dhont> python manage.py runserver
```

6 Creamos la carpeta `applications` a la altura de manage.py

![image](https://github.com/user-attachments/assets/6845ddc3-aae6-4593-a33e-0834d1d7665a)

![image](https://github.com/user-attachments/assets/04977199-7a94-4335-b3e0-07ad73bfd827)

7 Creamos la carpeta settings con su cuatro archivos interiores y borramos el settings original

![image](https://github.com/user-attachments/assets/a6303270-a68e-470a-9cfa-c4cbf7cdc77d)

8 Le indicamos a django que ejecute desde el entorno de configuración local.py:

9 Verificamos:

```bash
(entorno_4) C:\mis_proyectos\dhont> python manage.py runserver
```

10 Vamos al nivel de applications y creamos 4 nuevos proyectos:

```bash
(entorno_4) C:\mis_proyectos\dhont>cd applications
(entorno_4) C:\mis_proyectos\dhont\applications> django-admin startapp partidos
(entorno_4) C:\mis_proyectos\dhont\applications> django-admin startapp escanos
(entorno_4) C:\mis_proyectos\dhont\applications> django-admin startapp elecciones
(entorno_4) C:\mis_proyectos\dhont\applications> django-admin startapp votos
```

11  Ahora necesitamos instalar nuestras aplicaciones en el archivo base.py:

```
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
```

12 En cada uno de los archivos apps.py de las aplicaciones anteponemos el prefijo `applications.`:

Verificamos:

```
(entorno_4) C:\mis_proyectos\dhont> python manage.py runserver
```

13 Implementando la base de datos

```python
from django.db import models
from datetime import date

class Elecciones(models.Model):
   nombre = models.CharField("Nombre", max_length=50)
   fecha = models.DateField("Fecha", default=date.today)

   def __str__(self):
      return str(self.nombre) + "-" + str(self.fecha)
```

```python
from django.db import models

class Partidos(models.Model):
   nombre = models.CharField("Nombre", max_length=50)
   siglas = models.CharField("Nombre", max_length=50)

   def __str__(self):
      return self.nombre + "-" + self.siglas
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
      return str(self.escanos)
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
      return str(self.votos) 
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



Ahora conectamos Django a nuestra base de datos PostgreSQL:


Creamos una base de datos:

```
Server [localhost]:
Database [postgres]:
Port [5432]:
Username [postgres]:
Contraseña para usuario postgres:

psql (16.4)
ADVERTENCIA: El código de página de la consola (850) difiere del código
            de página de Windows (1252).
            Los caracteres de 8 bits pueden funcionar incorrectamente.
            Vea la página de referencia de psql «Notes for Windows users»
            para obtener más detalles.
Digite «help» para obtener ayuda.

postgres=#  CREATE DATABASE dhont101;
CREATE DATABASE
postgres=# \c dhont101;
Ahora está conectado a la base de datos «dhont101» con el usuario «postgres».
dhont101=# ALTER ROLE chris101 WITH PASSWORD 'nueva123456';
ALTER ROLE
dhont101=#
```


Check Database User Privileges

```sql
dhont101=# GRANT ALL PRIVILEGES ON SCHEMA public TO chris101;
GRANT
dhont101=# GRANT ALL PRIVILEGES ON DATABASE dhont101 TO chris101;
GRANT
dhont101=#
```





```
from .base import *

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dhont101',
        'USER': 'chris101',
        'PASSWORD': 'nueva123456',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}

STATIC_URL = 'static/'
```


```
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

Volvemos a crear un superuser:

```python
(entorno_4) C:\mis_proyectos\dhont> python manage.py createsuperuser
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

# La lógica del negocio.

1 La url http://127.0.0.1:8000/seleccionar-eleccion/

```
urlpatterns = [
   path('seleccionar-eleccion/', 
   views.SeleccionarEleccionView.as_view(),)
]
```

despliega un filtro de partidos por elección.

![image](https://github.com/user-attachments/assets/e58a29b9-07ba-49cd-bc5d-efb5c76d752a)

2 **SeleccionarEleccionView**

```
class SeleccionarEleccionView(FormView):
    template_name = 'votos/seleccionar_eleccion.html'
    form_class = SeleccionarEleccionForm

    def form_valid(self, form):
        eleccion = form.cleaned_data['eleccion']
        return redirect(reverse('votos_app:partidos_por_eleccion') + f'?eleccion={eleccion.id}')
```

Este código define una vista basada en clases llamada `SeleccionarEleccionView` que hereda de `FormView`, lo que significa que su propósito principal es manejar formularios. El atributo `template_name` especifica la plantilla HTML que se usará para renderizar la página asociada a esta vista, mientras que `form_class` apunta al formulario que esta vista utilizará, en este caso, `SeleccionarEleccionForm`. En el método `form_valid`, que se ejecuta cuando el formulario enviado es válido, se recupera el dato **eleccion** del formulario validado a través de `form.cleaned_data`. Luego, la vista redirige al usuario a una nueva URL generada dinámicamente utilizando reverse para **construir la ruta** a la vista llamada partidos_por_eleccion dentro de la aplicación votos_app. Se añade un parámetro de consulta (?eleccion=eleccion.id) para incluir el identificador de la elección seleccionada en la URL resultante, permitiendo que la siguiente vista acceda a este dato para procesarlo o mostrarlo según sea necesario.


```
app_name = "votos_app"
urlpatterns = [
      path('partidos/', 
      views.PartidosPorEleccionView.as_view(), 
      name='partidos_por_eleccion'),
]
```

```python

class PartidosPorEleccionView(FormView):

   template_name = 'votos/partidos_por_eleccion.html'
   form_class = VotosPorPartidoForm
   success_url = reverse_lazy('votos_app:exito')

   def get_form_kwargs(self):
      kwargs = super().get_form_kwargs()
      eleccion_id = self.request.GET.get('eleccion')  # Obtener la elección desde los parámetros GET
      eleccion = get_object_or_404(Elecciones, id=eleccion_id)
      partidos = Partidos.objects.filter(votos__eleccion=eleccion).distinct()
      kwargs['partidos'] = partidos  # Pasar los partidos al formulario dinámico
      self.eleccion = eleccion  # Guardar elección para usar en el contexto
      return kwargs

   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['eleccion'] = self.eleccion  # Pasa la elección al contexto
      return context


   def form_valid(self, form):
      for field_name, value in form.cleaned_data.items():
            if field_name.startswith('votos_'):  # Identificar los campos dinámicos
               partido_id = int(field_name.split('_')[1])
               partido = get_object_or_404(Partidos, id=partido_id)
               # Crear o actualizar los votos en la base de datos
               Votos.objects.update_or_create(
                  partido=partido,
                  eleccion=self.eleccion,
                  defaults={'votos': value}
               )
      return super().form_valid(form)  # Redirigir al listado o página de confirmación

```


Este código implementa una vista basada en formularios llamada PartidosPorEleccionView, que gestiona un flujo relacionado con elecciones y votos por partidos. La vista utiliza template_name para definir la plantilla HTML a usar, form_class para especificar la clase del formulario, y success_url para redirigir tras el envío exitoso del formulario. 

***

**El método get_form_kwargs**

```
   def get_form_kwargs(self):
      kwargs = super().get_form_kwargs()
      eleccion_id = self.request.GET.get('eleccion')  # Obtener la elección desde los parámetros GET
      eleccion = get_object_or_404(Elecciones, id=eleccion_id)
      partidos = Partidos.objects.filter(votos__eleccion=eleccion).distinct()
      kwargs['partidos'] = partidos  # Pasar los partidos al formulario dinámico
      self.eleccion = eleccion  # Guardar elección para usar en el contexto
      return kwargs
```

En el método get_form_kwargs, se extrae el parámetro eleccion de la solicitud GET, se busca el objeto correspondiente en la base de datos y se filtran los partidos relacionados con esta elección; estos partidos se pasan al formulario dinámicamente. Este método get_form_kwargs es una sobrescritura del método base proporcionado por la clase FormView. Su propósito es añadir datos adicionales al diccionario de argumentos (kwargs) que se pasa al formulario al crearlo. 

Llamada al método base:

kwargs = super().get_form_kwargs() llama al método original de la clase padre para obtener los argumentos predeterminados necesarios para inicializar el formulario. Esto garantiza que los argumentos existentes no se pierdan y se puedan extender.

Obtener el parámetro eleccion de la solicitud:

eleccion_id = self.request.GET.get('eleccion') busca en los parámetros GET de la solicitud HTTP el valor asociado a la clave eleccion. Este valor probablemente fue pasado como parte de la URL o una consulta.

Validación del identificador y obtención del objeto Elecciones:

eleccion = get_object_or_404(Elecciones, id=eleccion_id) verifica si existe un objeto en el modelo Elecciones con el ID proporcionado. Si no se encuentra, genera un error 404. Este paso asegura que el programa no falle por tratar de usar un objeto inexistente.

Filtrar partidos relacionados con la elección:

partidos = Partidos.objects.filter(votos__eleccion=eleccion).distinct() realiza una consulta en la base de datos para obtener los partidos asociados a la elección específica. Aquí, votos__eleccion establece una relación entre el modelo Partidos y el modelo Votos a través de la elección. El uso de distinct() garantiza que no se repitan resultados.

Añadir los partidos al diccionario kwargs:

kwargs['partidos'] = partidos añade la lista de partidos al diccionario de argumentos. Este dato será utilizado para configurar un formulario dinámico, donde la lista de partidos probablemente se mostrará como opciones.

Almacenar el objeto eleccion en el atributo de instancia:

self.eleccion = eleccion guarda el objeto Elecciones en un atributo de la instancia de la clase, lo cual permite que otros métodos de la vista accedan a este objeto más adelante, como en el contexto o en la lógica del formulario.

Devolver el diccionario actualizado:

return kwargs devuelve el diccionario completo, incluyendo tanto los datos originales obtenidos del método padre como los nuevos datos añadidos (los partidos).

***




El método get_context_data añade el objeto eleccion al contexto de la plantilla, facilitando su uso en la interfaz. 

Por último, form_valid procesa los datos del formulario, identifica campos que comienzan con "votos_" como campos dinámicos de entrada, asocia cada campo con el partido correspondiente usando su ID, y actualiza o crea registros en la base de datos mediante el modelo Votos. Luego, redirige al usuario a la URL de éxito configurada. Es una implementación que combina lógica de negocio, dinámica de formulario y persistencia de datos de forma eficiente.




***
***
<br>
<br>
<br>
<br>

<br>
<br>
<br>
<br>
***
***
























