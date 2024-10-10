# Comandos Úteis Utilizados no Desenvolvimento do Projeto

### Configurações Iniciais

```bash
mkdir django-project
```

Cria uma nova pasta  onde será armazenado o projeto.

```bash
cd nome-do-projeto
```

Entra na pasta criada, permitindo que você trabalhe dentro dessa pasta.

```bash
python -m venv .venv
```

Cria um ambiente virtual chamado `.venv`, onde serão instaladas as dependências do projeto sem interferir nas configurações globais do sistema.

```bash
source .venv/bin/activate` (Linux/macOS) ou `.\.venv\Scripts\activate` (Windows)
```

Ativa o ambiente virtual criado anteriormente, permitindo que você utilize as dependências instaladas nesse ambiente.

```bash
pip install Django
```

Instala o framework Django dentro do ambiente virtual, permitindo que você comece a desenvolver sua aplicação web com Django.

---

### Criação do Projeto e Aplicações

```bash
django-admin startproject nome-do-projeto-base
```

Cria um novo projeto Django, gerando a estrutura inicial do sistema.

```bash
cd nome-do-projeto-base
```

Entra na pasta do projeto base, onde está a estrutura criada.

```bash
python manage.py startapp nome-do-app
```

Cria um novo aplicativo  dentro do projeto Django, que será responsável por uma funcionalidade específica do sistema.

---

### Gerenciamento de Banco de Dados e Migrações

```bash
python manage.py migrate
```

Executa todas as migrações pendentes, aplicando as alterações no esquema do banco de dados.

```bash
python manage.py showmigrations
```

 Mostra o status das migrações, indicando quais foram aplicadas e quais estão pendentes.

```bash
python manage.py sqlmigrate surveys 0001
```

Exibe o SQL gerado pela migração `0001` do aplicativo criado, mostrando as queries que serão executadas no banco de dados.

---

### Comandos Úteis para Desenvolvimento

```bash
python manage.py runserver
```

Inicia o servidor de desenvolvimento do Django, permitindo testar a aplicação localmente.

```bash
python manage.py createsuperuser
```

Cria um superusuário com acesso ao painel de administração do Django.

```bash
python manage.py --help
```

Exibe uma lista com todos os comandos disponíveis e suas respectivas opções.

---

### Testes e Execução de Testes Específicos

```bash
python manage.py test
```

 Executa todos os testes automáticos do projeto para garantir que o código está funcionando conforme o esperado.

```bash
python manage.py test <app_name>.tests.<test_file>.<TestClassName>
```

Executa um teste específico localizado no arquivo de testes `<test_file>`.py, dentro da classe `<TestClassName>` do aplicativo `<app_name>`.

---

### PDB - Python Debugger

Para depurar seu código Python, você pode usar o PDB (Python Debugger). Para iniciar a depuração, execute:

```bash
import pdb; pdb.set_trace()
```

O PDB permite pausar a execução, inspecionar variáveis e definir pontos de interrupção. Para mais detalhes, consulte a [Documentação do PDB](https://docs.python.org/pt-br/dev/library/pdb.html)
