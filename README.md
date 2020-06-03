# django-Youtube

Simple You Tube Clone using [django](https://www.djangoproject.com/) and [MongoDB](https://www.mongodb.com/)



## Linux
```shell
pip install --upgrade pip setuptools
pip install -r requirements.txt
```
#### gunicorn --bind 127.0.0.1:8000 sistema.wsgi


## Windows
```shel
pip install --upgrade pip setuptools
pip install -r requirements.txt
pip install waitress
```
#### waitress-serve --listen=*:8000 sistema.wsgi:application
