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
python.exe -m pip install --upgrade pip
pip install django-ckeditor
pip install psycopg2-binary
pip install Pillow
```

4 Construimos la aplicacion:

```
(entorno_4) C:\mis_entornos\entorno_4\Scripts> cd \mis_proyectos
(entorno_4) C:\mis_proyectos> django-admin startproject dhont
```

y se crea la carpeta contenedora `dhont` en la carpeta `mis_proyectos`

5 Verificamos:

```
(entorno_4) C:\mis_proyectos>  cd \mis_proyectos\dhont
(entorno_4) C:\mis_proyectos\dhont> python manage.py runserver
```

6 Creamos la carpeta `applications` a la altura de manage.py





































