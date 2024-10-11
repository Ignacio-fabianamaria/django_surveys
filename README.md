# Django Surveys

Este projeto foi desenvolvido como parte do módulo Django do Bootcamp de Python & Django oferecido pela WoMakersCode, em parceria com o iFood, Potência Tech e Microsoft. O objetivo do projeto foi criar uma aplicação de pesquisas. O projeto Django Survey foi desenvolvido em aula prática para aplicar os conhecimentos teóricos sobre Django e testes em Python.
[Mais Mulheres Tech](https://www.maismulheres.tech/)

## Descrição

O `django_surveys` é um projeto em Django para gerenciar e exibir pesquisas, permitindo que os usuários visualizem uma lista de pesquisas disponíveis, vejam os detalhes de cada pesquisa, votem nas opções fornecidas e visualizem os resultados em forma de gráfico. O cadastro e a gestão das pesquisas são realizados através do Django Admin.

## Funcionalidades

- **Listagem de Pesquisas**: Exibe todas as pesquisas disponíveis para os usuários votarem.
- **Detalhes da Pesquisa**: Mostra as opções da pesquisa para o usuário escolher e votar.
- **Votação**: Os usuários podem votar em uma das opções disponíveis de cada pesquisa.
- **Gráfico de Resultados**: Após o voto, é exibido um gráfico detalhado com a quantidade de votos em cada opção.
- **Administração via Django Admin**: O cadastro e a gestão das pesquisas são realizados na interface administrativa do Django.

## Download do Projeto

1. **Clone o repositório**

```bash
   git clone https://github.com/Ignacio-fabianamaria/django_surveys.git
```

2. **Entre na pasta do projeto**

```bash
cd django_surveys
```

3. **Crie um ambiente virtual**

```bash
python -m venv .venv 
```

4. **Ative o ambiente virtual**

- Para Linux ou macOS

```bash
source .venv/bin/activate
```

- Para Windows

```bash
.\.venv\Scripts\activate
```

5. **Instale o Django**

```bash
pip install Django
```

6. **Entre na pasta do projeto base**

```bash
cd womakers
```

7. **Execute as migrações**

```bash
python manage.py migrate
```

8. **Crie um usuário do admin**

```bash
python manage.py createsuperuser
```

9. **Execute a aplicação**

```bash
python manage.py runserver
```

## Gráfico da Votação / Chart.js

![Gráfico Chart.js](http://aishelf.org/wp-content/uploads/2017/04/chartjs.jpg)

Chart.js é uma biblioteca JavaScript que cria gráficos interativos e animados em páginas web. Oferece uma variedade de tipos de gráficos, como barras, linhas e pizza, tornando a visualização de dados fácil e atrativa.

No projeto, o Chart.js foi escolhido para mostrar o gráfico de votos por sua facilidade de uso e capacidade de criar visualizações informativas. Isso ajuda os usuários a analisar os dados de votação de forma clara e melhora a compreensão das informações.

[Getting Started](https://www.chartjs.org/docs/latest/getting-started/) | [Pie Charts](https://www.chartjs.org/docs/latest/charts/doughnut.html#pie)

## Guia de Configuração e Desenvolvimento 

Para ajudar na configuração e no desenvolvimento do projeto Django, foi criado um guia detalhado. Este guia aborda todos os passos necessários, desde a criação do ambiente virtual até a integração do Bootstrap ao projeto

[Acesse o guia completo aqui](https://github.com/Ignacio-fabianamaria/django_surveys/blob/main/guia-configuracao-desenvolvimento-django.md)

## Comandos Úteis

Para facilitar o desenvolvimento do projeto, foi criado um documento contendo comandos úteis que podem ser utilizados durante o processo. Este documento serve como um guia prático, reunindo comandos que auxiliam na configuração, execução e manutenção do projeto.

[Acesse o documento de comandos úteis aqui](https://github.com/Ignacio-fabianamaria/django_surveys/blob/main/comandos_uteis.md)

##  Documentação

Para manter a organização e facilitar o entendimento do projeto, foi criado um documento que contém todos os links para a documentação utilizada ao longo do desenvolvimento. Este documento servirá como um repositório central de informações relevantes, funcionando como uma referência para auxiliar o estudo e o aprendizado.

[Acesse o documento aqui](https://github.com/Ignacio-fabianamaria/django_surveys/blob/main/links_uteis_documentacao.md)

## 🚧 Em Construção 🚧