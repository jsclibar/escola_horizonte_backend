# Atividade Prática – Desenvolvimento de uma API REST com FastAPI

**Tema:** Desenvolvimento de um CRUD utilizando Python e FastAPI  
**Modalidade:** Atividade em trios  
**Duração prevista:** 3 aulas de 50 minutos  
**Ferramentas:** Python, FastAPI, Pydantic e Swagger UI

---

## 1. Situação-problema

A **Biblioteca Comunitária Saber** precisa de um sistema para gerenciar seu acervo de livros.

Atualmente, o controle dos livros é realizado manualmente, dificultando o cadastro, a consulta, a atualização e a exclusão das informações.

Para solucionar esse problema, a biblioteca solicitou o desenvolvimento de uma **API REST** que permita realizar essas operações.

## 2. Desafio

Em trios, vocês deverão desenvolver o backend do sistema de gerenciamento de livros utilizando **Python e FastAPI**.

A aplicação deverá implementar as operações de um CRUD (Create, Read, Update e Delete), permitindo cadastrar, consultar, atualizar e excluir livros. Além disso, deverá permitir a consulta de livros pelo nome do autor.

**Importante:** nesta atividade, não será utilizado banco de dados. As informações deverão ser armazenadas temporariamente em uma lista Python.

Os trios poderão consultar o **repositório de exemplos disponibilizado no GitHub**.

O objetivo não é apenas reproduzir o exemplo apresentado, mas compreender seu funcionamento e aplicar os conhecimentos na construção de uma nova API.

## 3. Estrutura dos dados

Cada livro deverá possuir os seguintes atributos:

| Atributo | Tipo | Descrição |
|---|---|---|
| idlivro | int | Identificador único do livro |
| titulo | str | Título do livro |
| autor | str | Nome do autor |
| ano | int | Ano de publicação |

A aplicação deverá iniciar com pelo menos **dois livros cadastrados** na lista.

## 4. Requisitos funcionais

A API deverá disponibilizar os seguintes endpoints:

| Método HTTP | Endpoint | Funcionalidade |
|---|---|---|
| GET | `/` | Retornar uma mensagem de boas-vindas |
| GET | `/livros` | Listar todos os livros cadastrados |
| GET | `/livros/{idlivro}` | Consultar um livro pelo ID |
| GET | `/livros/autor/{nome}` | Consultar livros pelo nome do autor |
| POST | `/livros` | Cadastrar um novo livro |
| PUT | `/livros/{idlivro}` | Atualizar os dados de um livro |
| DELETE | `/livros/{idlivro}` | Excluir um livro |

A consulta por autor deverá retornar uma lista contendo todos os livros cadastrados que correspondam ao nome informado.

Por exemplo, ao realizar uma requisição para:

`GET /livros/autor/Machado%20de%20Assis`

A API deverá retornar todos os livros cadastrados do autor Machado de Assis.

## 5. Requisitos técnicos

Durante o desenvolvimento, o trio deverá:

1. Utilizar o framework **FastAPI** para construir a API.
2. Criar um modelo de dados utilizando **Pydantic (BaseModel)**.
3. Armazenar os livros em uma lista Python.
4. Implementar a geração automática de identificadores para novos livros.
5. Utilizar estruturas de repetição e condicionais para localizar os registros.
6. Utilizar **HTTPException** para retornar o código HTTP 404 quando um livro não for encontrado.
7. Retornar o código HTTP 201 quando um livro for cadastrado.
8. Organizar os endpoints e suas descrições na documentação automática do FastAPI.

## 6. Desenvolvimento da atividade

### Etapa 1 – Preparação do ambiente

Criar o projeto, preparar o ambiente Python e instalar as dependências necessárias.

### Etapa 2 – Estruturação da API

Criar a aplicação FastAPI, definir o modelo de dados com Pydantic e preparar a lista inicial de livros.

### Etapa 3 – Implementação dos endpoints

Desenvolver as operações de consulta, cadastro, atualização e exclusão dos livros, conforme os requisitos apresentados.

Implementar também a funcionalidade de consulta de livros pelo nome do autor.

### Etapa 4 – Testes e validação

Utilizar o Swagger UI, disponível em `/docs`, para testar as funcionalidades implementadas.

O trio deverá verificar se:

- É possível consultar todos os livros cadastrados.
- A consulta por ID retorna o livro correto.
- A consulta por autor retorna todos os livros correspondentes ao nome informado.
- Um novo livro pode ser cadastrado com ID gerado automaticamente.
- Os dados de um livro existente podem ser atualizados.
- Um livro pode ser excluído.
- A API retorna o erro HTTP 404 quando um livro não é encontrado.

## 7. Entrega da atividade

Cada trio deverá apresentar a API em funcionamento, demonstrando as operações implementadas por meio do Swagger UI.

Durante a apresentação, **todos os integrantes deverão participar**, demonstrando conhecimento sobre o código desenvolvido e explicando o funcionamento das principais operações.

O código-fonte também deverá ser disponibilizado para avaliação.

---

## 8. Rubricas de avaliação

A avaliação será realizada considerando o desenvolvimento da atividade, o funcionamento da API e a compreensão dos conceitos trabalhados.

| Critério | Atende plenamente | Atende parcialmente | Ainda não atende |
|---|---|---|---|
| **Estruturação da aplicação** | Organiza corretamente a aplicação FastAPI, o modelo de dados e a lista de livros. | Apresenta a estrutura básica, mas necessita de ajustes. | Não consegue estruturar adequadamente a aplicação. |
| **Implementação das funcionalidades** | Implementa corretamente todas as operações do CRUD e a consulta de livros por autor. | Implementa parte das operações ou apresenta falhas em algumas funcionalidades. | Não consegue implementar as operações básicas de gerenciamento e consulta dos livros. |
| **Tratamento de dados e erros** | Utiliza corretamente o Pydantic, a geração de IDs e os códigos de status HTTP. | Implementa esses recursos, mas apresenta inconsistências. | Não implementa adequadamente a validação, os identificadores ou o tratamento de erros. |
| **Testes e validação** | Testa e demonstra todas as funcionalidades utilizando o Swagger UI. | Realiza testes, mas não verifica todas as operações ou situações de erro. | Não realiza os testes necessários para validar a API. |
| **Compreensão e colaboração** | Todos os integrantes participam do desenvolvimento e demonstram compreender o funcionamento da API. | A participação ou a compreensão dos integrantes é desigual ou parcial. | O trio apresenta dificuldades significativas para explicar a solução desenvolvida. |

---

## 9. Orientações importantes

Esta atividade será desenvolvida **em trios**, sendo permitida a consulta ao repositório de exemplos no GitHub.

Espera-se que vocês consigam interpretar os requisitos, adaptar os conhecimentos já adquiridos e construir uma API REST funcional, contemplando todas as operações de gerenciamento e consulta dos livros.

Todos os integrantes deverão participar ativamente das etapas de desenvolvimento, testes e apresentação.

**O foco da avaliação será a capacidade de aplicar os conhecimentos na resolução do problema proposto, compreender o funcionamento da solução e trabalhar de forma colaborativa.**