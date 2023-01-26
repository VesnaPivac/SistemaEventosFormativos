# Sistema-de-Gestion-de-Eventos-Formativos-UNISON
Web Application Project for Objet Oriented Analysis and Design subject

## Contributors:
### Alberto Leyva  (JosephLeyva) 
### Vesna Pivac (VesnaPivac)




------------------------------------------------------------------
# Instalar un Virtual Environment (Recomendación)
Un entorno virtual es un lugar en su sistema donde puede instalar paquetes y aislarlos de todos los demás paquetes de Python.
Es recomendable crear un entorno virtual en la carpeta donde estaremos trabajando
```
# Primero tenemos que instalar virtualenv
pip install virtualenv

# Luego creamos el virtual environment con el nombre que queramos
virtualenv cc_env
```
## Activar el Virtual Environment
```
cc_env\scripts\activate
```
Una vez activado, podemos instalar Django ahí
Para verificar que lo hemos activado, se verá el nombre del virtualenv antes de la ruta
![image](https://user-images.githubusercontent.com/43888961/139622813-49883cca-3035-48e6-8fea-1760de5c9d46.png)

## Desactivar Virtual Environment
Para desactivar el entorno virtual y volver a la cmd principal ejecutamos:
```
cc_env\scripts\deactivate
```

-------------------------------------------------------------------
# Instalar Django
## Requisitos
Tener `python` y `pip` instalado en la computadora

## Checar Versión
Primero chequemos que tenemos Django instalado:
`python -m django --version`

Si, tenemos Django instalado, sale la versión de su instalación. Si no es así, saldrá un error que dice  `No module named django`

## Instalación

`python -m pip install Django`

----------------------------------------------------------------------------------------
# Creación del Proyecto
Para crear un nuevo proyecto ejectuamos:
```
django-admin startproject cursos_unison
```
Vemos que se crean los siguientes archivos:
```
cursos_unison/
    manage.py
    cursos_unison/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
```
## Ejecutar Servidor de Django
Nos movemos a la carpeta cursos_unison/
```
cd cursos_unison
```
Ejecutamos el siguiente comando:
```
python manage.py runserver
```

Al ejecutar el servidor, nos manda la liga http://127.0.0.1:8000/
Al entrar ahí y pegarla en algún navegador debe de aparecernos la siguiente ventana
![image](https://user-images.githubusercontent.com/43888961/139624729-5610a044-0c8c-4334-b352-2d3dedf2702a.png)
