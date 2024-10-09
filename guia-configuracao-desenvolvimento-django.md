# Guia de Configuração e Desenvolvimento de Projeto Django

Este guia fornece os passos necessários para configurar e iniciar o desenvolvimento de um projeto Django. Foi criaado um projeto chamado `womakers` e um aplicativo chamado `surveys`.

## 1. Criando um Ambiente Virtual

Para isolar as dependências do projeto, é recomendável usar um ambiente virtual. Para isso, é necessarios executar os seguintes comandos:

#### Para Linux e macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

#### Para Windows

```bash
python -m venv .venv
.\.venv\Scripts\activate
```

## 2. Instalando o Django

Com o ambiente virtual ativo, o próximo passo é instalar o Django usando o comando:

```bash
pip install Django
```

## 3. Criando um Novo Projeto Django

Agora que o Django está instalado, o próximo passo é criar um novo projeto. O projeto `womakers` será a base para do aplicativo de gerenciamento de pesquisas. Ao criar um projeto Django, é possível estabelecer uma estrutura que facilitará a organização e o desenvolvimento das funcionalidades desejadas.

Para criar o projeto, execute os seguintes comandos:

```bash
django-admin startproject womakers
cd womakers/
```

## 4. Criando um Novo Aplicativo Django

Com o projeto criado, o próximo passo é criar um aplicativo que será responsável por gerenciar as pesquisas. Em Django, um projeto pode conter múltiplos aplicativos, cada um com sua própria funcionalidade.

Para criar um novo aplicativo chamado `surveys`, execute:

```bash
python manage.py startapp surveys
```

## 5. Configurando o Banco de Dados

Antes de criar as tabelas do banco de dados, é necessário executar as migrações iniciais. Este processo aplica as migrações padrão do Django e configura o banco de dados, preparando-o para armazenar dados.

```bash
python manage.py migrate
```

## 6. Criando um Superusuário

Para acessar o painel administrativo do Django, é necessário criar um superusuário. Ao rodar o comando de criação, será solicitado  fornecer um nome de usuário, e-mail e senha para o superusuário. Isso permitirá  gerenciar o projeto através da interface administrativa do Django.

```bash
python manage.py createsuperuser
```

## 7. Adicionando o Aplicativo surveys às Aplicações Instaladas

Para que o Django reconheça o aplicativo criado, neste caso o app surveys, é necessário registrá-lo no arquivo `settings.py`, localizado na pasta do projeto base "womakers". Isso é feito adicionando o nome do aplicativo à lista de `INSTALLED_APPS`, o que permite que o Django registre suas configurações e modelos, integrando-o ao projeto

Exemplo:

```bash
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "surveys",
]
```

## 8. Criando Migrações para o Aplicativo surveys

Após definir seus modelos no aplicativo surveys, é necessário criar e aplicar as migrações. O comando `makemigrations` surveys gera arquivos de migração com base nas alterações feitas nos modelos do aplicativo. Em seguida, o comando `migrate` aplica essas migrações ao banco de dados, garantindo que a estrutura esteja atualizada.

```bash
python manage.py makemigrations surveys
python manage.py migrate
```

## 9. Configurando o Admin do Django

Após criar os modelos, é fundamental configurar o arquivo admin.py dentro do aplicativo `surveys` para registrar os modelos no painel administrativo do Django. Isso permitirá que você gerencie facilmente os dados do seu aplicativo por meio da interface administrativa.

Para visualizar a estrutura necessária, consulte o arquivo localizado em: [womakers/surveys/admin.py](https://github.com/Ignacio-fabianamaria/django_surveys/blob/main/womakers/surveys/admin.py)

## 10. Configurando URLs

No arquivo urls.py da pasta do projeto principal `womakers`, é necessário importar a função include e adicionar um novo caminho que inclua as URLs do aplicativo `surveys`. Isso garantirá que as rotas definidas no aplicativo sejam acessíveis a partir do projeto principal.

Abaixo está um exemplo deste processo:

```bash
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('surveys.urls')),
]
```

#### Explicação:

A linha `path("", include('surveys.urls'))` desempenha um papel crucial na integração do aplicativo surveys ao projeto principal, assegurando que as URLs do aplicativo surveys sejam corretamente mapeadas e acessíveis,

- **path("")**: Define que as URLs do aplicativo surveys estarão acessíveis a partir da raiz do projeto (ou seja, diretamente na URL principal do site).

- **include('surveys.urls')**: Instruí o Django a buscar as definições de URL no arquivo urls.py do aplicativo surveys. Isso permite que todas as rotas definidas nesse arquivo sejam automaticamente incluídas nas URLs do projeto, facilitando o gerenciamento e a organização das rotas de cada aplicativo.

## 11. Criando URLs no Aplicativo surveys

Para gerenciar as rotas do aplicativo `surveys`, é necessário criar um arquivo `urls.py` na pasta do aplicativo. Este arquivo será responsável por definir as URLs específicas que o aplicativo irá utilizar, facilitando a navegação e a organização das requisições.

 Para visualizar um exemplo de como estruturar o arquivo, consulte: [womakers/surveys/urls.py](https://github.com/Ignacio-fabianamaria/django_surveys/blob/main/womakers/surveys/urls.py).

## 12. Estruturando Templates

No Django, `templates` são arquivos HTML que permitem a renderização dinâmica de conteúdo no frontend, utilizando variáveis, filtros e tags. Eles são essenciais para criar interfaces interativas e dinâmicas a partir de dados enviados pelas views.

Dentro do aplicativo `surveys`, foi criado uma pasta chamada templates para armazenar todos os arquivos de templates do app. Em seguida, dentro dessa pasta, foi criado uma subpasta específica para o aplicativo, que geralmente é nomeada com o mesmo nome do aplicativo.

``` markdown
womakers/
└── surveys/
    └── templates/
        └── surveys/
```

_**OBS** É uma **boa prática** no Django que cada aplicativo tenha sua própria subpasta dentro de `templates`. Isso ajuda a evitar conflitos de nomes e facilita o gerenciamento de arquivos em projetos que contêm múltiplos aplicativos. Essa organização permite que o Django encontre facilmente os templates corretos para cada aplicação, utilizando o caminho apropriado._

## 13. Criando Templates Necessários

Dentro da pasta `surveys/templates/surveys`, deve-se criar os templates necessários para o funcionamento do aplicativo. Para este projeto, criado três arquivos de templates:

- **base.html**: Este é o template base que fornece a estrutura fundamental da página, incluindo a configuração de cabeçalho.

- **question_list.html**: Este template exibe a lista de pesquisass disponíveis, permitindo que os usuários todas as pesquisas habilitadas cadastradas no sistema.

- **question_detail.html**: Este template apresenta os detalhes de uma pesquisa específica, permitindo que os usuários visualizem as opções de resposta disponíveis e escolham uma alternativa para votar.

## 14. Iniciando Testes

No Django, os testes são fundamentais para garantir que o comportamento do aplicativo funcione corretamente. Embora o Django ofereça suporte nativo para testes, como o comando para executá-los, o desenvolvedor é responsável por criar a estrutura de testes, incluindo arquivos e pastas.

Neste projeto, a pasta `womakers/surveys/tests/` foi criada manualmente para organizar os testes, e três arquivos específicos foram adicionados:

- **tests_models.py**: Contém testes para os modelos, verificando se os dados estão sendo processados corretamente.
- **tests_details_view.py**: Testa a view de detalhes, garantindo que as informações corretas sejam exibidas ao acessar uma pesquisa específica.
- **tests_list_views.py**: Focado na view de listagem, assegurando que as pesquisas cadastradas sejam apresentadas adequadamente.

Para mais informações sobre como criar e executar testes, consulte a [documentação oficial do Django](https://docs.djangoproject.com/en/5.1/topics/testing/overview/).

## 15. Integrando Bootstrap ao Projeto Django

Para melhorar o visual e a experiência do usuário no projeto, é possível integrar o Bootstrap, um framework de front-end que facilita a criação de interfaces.

##### Instalando o Bootstrap no Projeto Django
Primeiramente, instale o pacote django-bootstrap-v5 usando o comando pip:

```bash
pip install django-bootstrap-v5
```

##### Configurando o Bootstrap no Projeto

Depois de instalar o pacote, é precisa configurá-lo para que o Django o reconheça e aplique o Bootstrap nos templates. Para isso, adicione o bootstrap5 à lista de INSTALLED_APPS no arquivo settings.py:

```bash
INSTALLED_APPS = [
    # outras aplicações
    "bootstrap5",
    # outras aplicações
]
```

