#Guia de Configuração e Desenvolvimento de Projeto Django

python3 -m venv .venv
source .venv/bin/activate
pip install Django
django-admin startproject womakers
cd womakers/
python manage.py startapp surveys
python manage.py migrate
python manage.py createsuperuser

- installed apps
adicionar o app criando (surveys) no arquivo settings dentro da pasta do projeto principal na lista de "INSTALLED_APPS"

```bash
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "surveys"
]
```
após a adição do app surveys, rodar os comandos makemigrations e migrate
python manage.py makemigrations surveys
python manage.py migrate

Após criar as models no app surveys configurar o arquivo admin no surveys app.