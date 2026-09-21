# Backend (API) da Escola Horizonte

Projeto didático desenvolvido em **Python com FastAPI** para demonstrar conceitos básicos de desenvolvimento de APIs e integração com banco de dados MySQL.

## Tecnologias

- Python
- FastAPI
- Uvicorn
- MySQL

## Estrutura do projeto

```text
escola_horizonte_backend/
│
├── 01-conceitos_iniciais/
│   └── hello_world_fastapi.py
│
├── BD/
│   └── cria_banco.sql
│
├── .gitignore
├── README.md
└── requirements.txt
```

> A pasta `.venv` contém o ambiente virtual Python e não deve ser versionada no Git.

## Preparando o ambiente

Antes de executar o projeto, utilize um **ambiente virtual Python**.

O ambiente virtual pode ser criado e configurado diretamente pela IDE, como PyCharm ou VS Code.

Também é possível criá-lo pelo terminal:

```bash
python -m venv .venv
```

Após criar o ambiente virtual, certifique-se de que ele esteja selecionado/ativado antes de instalar as dependências.

## Instalando as dependências

Com o ambiente virtual configurado:

```bash
pip install -r requirements.txt
```

As principais dependências utilizadas são:

- `fastapi` - framework utilizado para desenvolver a API.
- `uvicorn` - servidor ASGI utilizado para executar a aplicação.

## Exemplo inicial

O primeiro exemplo está localizado em:

```text
00-conceitos_iniciais/
```

O arquivo `hello_world_fastapi.py` contém uma aplicação FastAPI simples com duas rotas:

```text
GET /          → Hello World
GET /alunos    → Lista de alunos
```

A aplicação pode ser executada diretamente pela IDE ou pelo terminal.

Pelo terminal:

```bash
python hello_world_fastapi.py
```

Após iniciar, a API estará disponível em:

```text
http://127.0.0.1:8000
```

## Documentação da API

O FastAPI gera automaticamente uma documentação interativa utilizando o padrão OpenAPI.

Com a aplicação em execução, acesse:

```text
http://127.0.0.1:8000/docs
```

A documentação permite visualizar e testar os endpoints disponíveis.

## Banco de dados

O script de criação do banco está localizado em:

```text
BD/cria_banco.sql
```

O banco inicial possui as tabelas `ALUNO` e `TELEFONE`.

O relacionamento entre elas é **1:N (um para muitos)**:

```text
ALUNO 1 ─────── N TELEFONE
```

Um aluno pode possuir vários telefones.