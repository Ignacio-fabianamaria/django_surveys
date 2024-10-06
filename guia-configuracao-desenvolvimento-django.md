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
python manage.py showmigrations

Após criar as models no app surveys configurar o arquivo admin no surveys app.

Cadastrar uma url no arquivo url na pasta do projeto principal [womakers] antes de configurar uma view.
no arquivi URL da pasta do projeto princial, importe o 'include' e adicione um novo path para incluir as urls dos apps criados

```bash
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('surveys.urls')),
]
```

Após , crieum arquivo url na pasta do app [surveys] e adicione as configurações necessarias

Crie na pasta no app [surveys], uma pasta chamada templates conter todas as templates de cada app do projeto.
Dentro da pasta template crie uma pasta para conter todos os templates do app [surveys].(OBS: Dentro da pasta template devera ter uma pasta para cada app criado ao longo do projeto)
Dentro na pasta do app dentro da pasta template [surveys] crie os templates necessarios.