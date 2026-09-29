
<p align="center">
  🇧🇷 <strong>Português</strong> |
  <a href="README.en.md">🇺🇸 English</a>
</p>

# 📝 FastAPI To-Do List

<p align="center">
  <strong>REST API para gerenciamento de tarefas desenvolvida com Python, FastAPI e SQLAlchemy.</strong>
</p>

<p align="center">
  Projeto desenvolvido para praticar conceitos de desenvolvimento Backend, APIs REST, persistência de dados e autenticação.
</p>

---

## 🚀 Sobre o projeto

O **FastAPI To-Do List** é uma API REST para gerenciamento de tarefas, desenvolvida utilizando **Python e FastAPI**.

O projeto utiliza **SQLAlchemy ORM** para comunicação com um banco de dados **SQLite**, **Pydantic** para validação dos dados e **HTTP Basic Authentication** para controle de acesso aos endpoints.

A aplicação implementa as principais operações de um sistema CRUD:

> **Create → Read → Update → Delete**

Além disso, possui paginação na listagem das tarefas e tratamento de erros HTTP.

---

## 🛠️ Tecnologias

| Tecnologia          | Utilização                              |
| ------------------- | --------------------------------------- |
| 🐍 **Python 3.12+** | Linguagem principal                     |
| ⚡ **FastAPI**       | Desenvolvimento da API REST             |
| 🗄️ **SQLAlchemy**  | ORM e comunicação com o banco           |
| 💾 **SQLite**       | Banco de dados                          |
| 📦 **Pydantic**     | Validação e modelagem dos dados         |
| 🔐 **HTTP Basic**   | Autenticação                            |
| 📚 **Poetry**       | Gerenciamento do projeto e dependências |

As dependências principais do projeto estão definidas no `pyproject.toml`, incluindo FastAPI, SQLAlchemy, Pydantic e aiosqlite.

---

## ✨ Funcionalidades

* [x] Criar tarefas
* [x] Listar tarefas
* [x] Buscar tarefa por ID
* [x] Atualizar tarefas
* [x] Excluir tarefas
* [x] Marcar tarefa como concluída
* [x] Paginação
* [x] Autenticação HTTP Basic
* [x] Validação de dados
* [x] Persistência em banco de dados
* [x] Tratamento de erros HTTP
* [x] Prevenção de tarefas duplicadas

---

## 🏗️ Estrutura da aplicação

A aplicação segue uma estrutura simples de backend, separando as principais responsabilidades entre:

```text
Cliente
   │
   ▼
FastAPI
   │
   ├── Autenticação
   │
   ├── Validação ───────► Pydantic
   │
   ├── Rotas CRUD
   │
   ▼
SQLAlchemy ORM
   │
   ▼
SQLite
```

O SQLAlchemy é responsável pelo mapeamento da entidade de tarefas e pela comunicação com o banco de dados.

---

## 📌 API Endpoints

### 🔐 Autenticação

Os endpoints utilizam **HTTP Basic Authentication**.

```text
Username: admin
Password: admin
```

> ⚠️ As credenciais utilizadas atualmente possuem finalidade educacional. Em uma aplicação de produção, elas devem ser armazenadas de forma segura e não diretamente no código-fonte.

---

### 📋 Listar tarefas

```http
GET /tarefas
```

Suporta paginação através dos parâmetros:

```http
GET /tarefas?page=1&limit=10
```

Exemplo de resposta:

```json
{
    "page": 1,
    "limit": 10,
    "total": 2,
    "tarefas": [
        {
            "id": 1,
            "nome_tarefa": "Estudar FastAPI",
            "descricao_tarefa": "Estudar desenvolvimento de APIs",
            "status_tarefa": false
        }
    ]
}
```

---

### 🔎 Buscar tarefa

```http
GET /tarefas/{id_tarefa}
```

Exemplo:

```http
GET /tarefas/1
```

---

### ➕ Criar tarefa

```http
POST /adicionar_tarefas
```

Body:

```json
{
    "nome_tarefa": "Estudar SQLAlchemy",
    "descricao_tarefa": "Aprender ORM com SQLAlchemy",
    "status_tarefa": false
}
```

O campo `status_tarefa` possui `false` como valor padrão.

---

### ✏️ Atualizar tarefa

```http
PUT /atualizar_tarefas/{id_tarefa}
```

Exemplo:

```json
{
    "status_tarefa": true
}
```

Os campos da tarefa podem ser atualizados individualmente.

---

### 🗑️ Excluir tarefa

```http
DELETE /deletar_tarefas/{id_tarefa}
```

Exemplo:

```http
DELETE /deletar_tarefas/1
```

---

## 🗃️ Modelo de dados

A entidade principal da aplicação é a tabela `Tarefas`.

```text
┌──────────────────────────────┐
│           Tarefas            │
├──────────────────────────────┤
│ id              INTEGER PK   │
│ nome_tarefa     VARCHAR      │
│ descricao_tarefa VARCHAR     │
│ status_tarefa   BOOLEAN      │
└──────────────────────────────┘
```

O modelo possui `id`, nome, descrição e status da tarefa.

---

## 🧩 Modelos Pydantic

O projeto utiliza modelos diferentes para criação, atualização e resposta da API.

### Criação

```python
class TarefaCreate(BaseModel):
    nome_tarefa: str
    descricao_tarefa: str
    status_tarefa: bool = False
```

### Atualização

```python
class TarefaUpdate(BaseModel):
    nome_tarefa: Optional[str] = None
    descricao_tarefa: Optional[str] = None
    status_tarefa: Optional[bool] = None
```

Essa abordagem permite realizar atualizações parciais dos dados da tarefa.

---

## 🔄 Fluxo de uma requisição

Exemplo de criação de uma tarefa:

```text
Cliente
   │
   │ POST /adicionar_tarefas
   ▼
FastAPI
   │
   ├── HTTP Basic Authentication
   │
   ├── Pydantic Validation
   │
   ▼
TarefaCreate
   │
   ▼
SQLAlchemy
   │
   ▼
SQLite
   │
   ▼
Resposta HTTP
```

---

## ⚙️ Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/NewEraM/FastApi-Ebac.git
```

### 2. Acesse o projeto

```bash
cd FastApi-Ebac
```

### 3. Instale as dependências

Utilizando Poetry:

```bash
poetry install
```

### 4. Execute a aplicação

```bash
poetry run fastapi dev ToDoList.py
```

A API ficará disponível em:

```text
http://127.0.0.1:8000
```

---

## 📖 Documentação

O FastAPI gera automaticamente a documentação da API.

### Swagger UI

```text
http://127.0.0.1:8000/docs
```

### ReDoc

```text
http://127.0.0.1:8000/redoc
```

A documentação permite visualizar os endpoints, seus parâmetros, modelos e testar as requisições diretamente pelo navegador.

---

## 📂 Estrutura do projeto

```text
FastApi-Ebac/
│
├── ToDoList.py
├── tarefas.db
├── pyproject.toml
├── poetry.lock
└── README.md
```

---

## 🧠 Conceitos aplicados

Este projeto foi desenvolvido como parte da minha evolução no desenvolvimento Backend com Python.

Durante sua construção, pratiquei:

* Desenvolvimento de APIs REST
* FastAPI
* Pydantic
* SQLAlchemy ORM
* SQLite
* CRUD
* HTTP Methods
* Dependency Injection com `Depends`
* Autenticação HTTP Basic
* Paginação
* Validação de dados
* Tratamento de exceções
* Gerenciamento de sessões do banco
* Poetry
* Organização de uma aplicação backend

---

## 🔮 Próximos passos

Pretendo evoluir o projeto adicionando:

* [ ] Autenticação com JWT
* [ ] Cadastro e gerenciamento de usuários
* [ ] Hash de senhas
* [ ] Filtros de tarefas
* [ ] Ordenação de resultados
* [ ] Busca por nome
* [ ] Testes automatizados com Pytest
* [ ] Separação em camadas (`routers`, `models`, `schemas`, `services`)
* [ ] Docker
* [ ] Deploy da API

---

## 👨‍💻 Autor

### Guilherme Muniz

Desenvolvedor em formação com foco em **Backend Python**, desenvolvimento de APIs e construção de aplicações web.

📧 **Email:** [muniz_157@outlook.com](mailto:muniz_157@outlook.com)

💻 **GitHub:** [NewEraM](https://github.com/NewEraM)

🔗 **LinkedIn:** [Guilherme Muniz | LinkedIn](https://linkedin.com/in/guilherme-muniz-8188a024/)

---

## ⭐ Feedback

Este projeto faz parte da minha jornada de aprendizado em **Python e desenvolvimento Backend**.

Feedbacks, sugestões e contribuições são sempre bem-vindos!
