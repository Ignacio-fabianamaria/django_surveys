# Guia de Configuração e Desenvolvimento de Projeto Django

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

- iniciando os testes:
python manage.py test
Por padrao o django cria uma pasta com nome test.py no aplicativo criado no projeto [surveys]

bootstraps 
pip install django-bootstrap-v5
Add to INSTALLED_APPS in your settings.py:

INSTALLED_APPS = (
    # ...
    "bootstrap5",
    # ...
)
# __________________________________________________

Download do projeto
git clone https://github.com/rafaelassacconi/django-project.git - clona o repositório
cd django-project - entra na pasta do projeto
python -m venv .venv - cria virtualenv
source .venv/bin/activate ou .\.venv\Scripts\activate - ativa virtualenv
pip install Django - instala Django
cd womakers - entra na pasta do sistema
python manage.py migrate - executa migrações
python manage.py createsuperuser - cria usuário do admin
python manage.py runserver - executa aplicação
Comandos
Criação do projeto
mkdir django-project - cria pasta do projeto
cd django-project - entra na pasta do projeto
python -m venv .venv - cria virtualenv
source .venv/bin/activate ou .\.venv\Scripts\activate - ativa virtualenv
pip install Django - instala Django
Criação da aplicação
django-admin startproject womakers - cria projeto Django
cd womakers - entra na pasta do sistema
python manage.py startapp surveys - cria app
Migrações
python manage.py migrate - executa migrações
python manage.py showmigrations - mostra status das migrações
python manage.py sqlmigrate surveys 0001 - mostra SQL da migração
Outros
python manage.py runserver - executa aplicação
python manage.py createsuperuser - cria usuário do admin
python manage.py --help - ver opções de comandos
python manage.py shell - executa o console
python manage.py test - executa os testes
python manage.py test surveys.tests.test_models.QuestionTestCase - executa um teste específico

# ________________________________________________________