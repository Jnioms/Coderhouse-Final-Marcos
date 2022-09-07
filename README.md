# Entrega Final - Juan Ignacio Marcos

Entrega final del trabajo final del curso de Python hecho en Coder House.

## Instrucciones

Primero es necesario instalar Django utilizando el comando [pip](https://pip.pypa.io/en/stable/) desde la terminal

```bash
> pip install django
```

## Uso

Para correr el projecto, es necesario utilizar el comando cd hasta estar en el mismo directorio del archivo manage.py

```bash
> cd /Directorio/
```

```
> ls
blog EntregaFinalCoder media messageboard static templates userprofile .env db.sqlite3 manage.py requirements.txt
```

Luego hay que hacer las migraciones de los modelos para crear la base de datos

```
> python manage.py makemigrations
> python manage.py migrate
```

Una vez hecho todo esto, ya esta listo para correrse. Por default hay que acceder a la web desde la ip 127.0.0.1:8000 (si no se cargan las variables de ejecucion)

```
> python manage.py runserver
```

Los index de las aplicaciones muestran todos los elementos de cada base de datos. Es posible que parezca vacio, pero una vez cargado los elementos, van a poder verse.


## Colabora

Si encontras algun error o bug en la pagina, por favor ayudame a mejorar reportandolo [en el repositorio](https://github.com/Jnioms/Coderhouse-Final-Marcos/issues). Muchas gracias! :)

## FAQs

**Como hiciste ese template?**

Tome cosas que me gustaban de [bootstrap-dark-5](https://vinorodrigues.github.io/bootstrap-dark-5/) que esta basado en Bootstrap 5 pero con Dark Mode para hacer mi propio template, y use partes de las docs de Bootstrap

---
**Como cambio las configuraciones?**

En el settings.py dentro de /EntregaFinalCoder/ estan la mayoria de configuraciones para agregar o sacar apps, deshabilitar el modo DEBUG y cambiar los path de los templates por ejemplo.
Tambien es necesario crear un .env con las configuraciones de SECRET_KEY, EMAIL_HOST, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, ADMIN_EMAIL. No lo muestro en el video pero esta andando el envio de reseteo de contraseña con un servidor web que tengo registrado localmente.

Para mas informacion acerca de Django, pueden utilizar la documentacion: [https://docs.djangoproject.com/en/4.1/](https://docs.djangoproject.com/en/4.1/)

---
**Como agrego mas objetos a la base de datos?**

Pueden crear un usuario administrador y agregarlos desde el panel ubicado en URL/admin/
Para crear al superusuario hay que usar el comando 

```
> python manage.py createsuperuser
```

Sino pueden crearse objetos usando el formulario de Sign Up en la parte superior derecha.

---
**Como me puedo inscribir al curso?**

[https://www.coderhouse.com/online/python](https://www.coderhouse.com/online/python)

## Link al video de youtube:

[Muestra del funcionamiento de la pagina web](https://www.youtube.com/watch?v=gIofkC6OeH0)

## Licencia
[GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/)
