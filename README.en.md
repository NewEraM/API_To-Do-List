# 📝 FastAPI To-Do List

<p align="center">
  <strong>REST API for task management built with Python, FastAPI, and SQLAlchemy.</strong>
</p>

<p align="center">
  A project developed to practice Backend development, REST APIs, data persistence, and authentication.
</p>

---

## 🚀 About the Project

**FastAPI To-Do List** is a REST API for task management, developed using **Python and FastAPI**.

The project uses **SQLAlchemy ORM** to communicate with a **SQLite** database, **Pydantic** for data validation, and **HTTP Basic Authentication** for endpoint access control.

The application implements the main operations of a CRUD system:

> **Create → Read → Update → Delete**

It also includes pagination for task listing and HTTP error handling.

---

## 🛠️ Technologies

| Technology          | Purpose                           |
| ------------------- | --------------------------------- |
| 🐍 **Python 3.12+** | Main programming language         |
| ⚡ **FastAPI**       | REST API development              |
| 🗄️ **SQLAlchemy**  | ORM and database interaction      |
| 💾 **SQLite**       | Database                          |
| 📦 **Pydantic**     | Data validation and modeling      |
| 🔐 **HTTP Basic**   | Authentication                    |
| 📚 **Poetry**       | Project and dependency management |

The project's main dependencies are defined in `pyproject.toml`, including FastAPI, SQLAlchemy, Pydantic, and aiosqlite.

---

## ✨ Features

* [x] Create tasks
* [x] List tasks
* [x] Get a task by ID
* [x] Update tasks
* [x] Delete tasks
* [x] Mark tasks as completed
* [x] Pagination
* [x] HTTP Basic Authentication
* [x] Data validation
* [x] Database persistence
* [x] HTTP error handling
* [x] Duplicate task prevention

---

## 🏗️ Application Architecture

The application follows a simple backend architecture:

```text
Client
   │
   ▼
FastAPI
   │
   ├── Authentication
   │
   ├── Validation ───────► Pydantic
   │
   ├── CRUD Routes
   │
   ▼
SQLAlchemy ORM
   │
   ▼
SQLite
```

SQLAlchemy is responsible for mapping the task entity and communicating with the database.

---

## 📌 API Endpoints

### 🔐 Authentication

The API endpoints use **HTTP Basic Authentication**.

```text
Username: admin
Password: admin
```

> ⚠️ The credentials currently used in the project are intended for educational purposes. In a production application, credentials should be securely stored and never hard-coded into the source code.

---

### 📋 List Tasks

```http
GET /tarefas
```

The endpoint supports pagination through query parameters:

```http
GET /tarefas?page=1&limit=10
```

Example response:

```json
{
    "page": 1,
    "limit": 10,
    "total": 2,
    "tarefas": [
        {
            "id": 1,
            "nome_tarefa": "Study FastAPI",
            "descricao_tarefa": "Study API development",
            "status_tarefa": false
        }
    ]
}
```

The API implements `page` and `limit` parameters and returns the total number of tasks.

---

### 🔎 Get Task by ID

```http
GET /tarefas/{id_tarefa}
```

Example:

```http
GET /tarefas/1
```

---

### ➕ Create a Task

```http
POST /adicionar_tarefas
```

Request body:

```json
{
    "nome_tarefa": "Study SQLAlchemy",
    "descricao_tarefa": "Learn ORM with SQLAlchemy",
    "status_tarefa": false
}
```

The `status_tarefa` field defaults to `false`.

---

### ✏️ Update a Task

```http
PUT /atualizar_tarefas/{id_tarefa}
```

Example:

```json
{
    "status_tarefa": true
}
```

The task fields can be updated individually.

---

### 🗑️ Delete a Task

```http
DELETE /deletar_tarefas/{id_tarefa}
```

Example:

```http
DELETE /deletar_tarefas/1
```

---

## 🗃️ Data Model

The main entity of the application is the `Tarefas` table.

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

The model contains an ID, task name, description, and completion status.

---

## 🧩 Pydantic Models

The project uses separate Pydantic models for task creation, updates, and API responses.

### Task Creation

```python
class TarefaCreate(BaseModel):
    nome_tarefa: str
    descricao_tarefa: str
    status_tarefa: bool = False
```

### Task Update

```python
class TarefaUpdate(BaseModel):
    nome_tarefa: Optional[str] = None
    descricao_tarefa: Optional[str] = None
    status_tarefa: Optional[bool] = None
```

This approach allows individual task fields to be updated without requiring all fields in the request.

---

## 🔄 Request Flow

Example of a task creation request:

```text
Client
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
HTTP Response
```

---

## ⚙️ Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/NewEraM/FastApi-Ebac.git
```

### 2. Navigate to the project

```bash
cd FastApi-Ebac
```

### 3. Install dependencies

Using Poetry:

```bash
poetry install
```

### 4. Run the application

```bash
poetry run fastapi dev ToDoList.py
```

The API will be available at:

```text
http://127.0.0.1:8000
```

---

## 📖 API Documentation

FastAPI automatically generates interactive API documentation.

### Swagger UI

```text
http://127.0.0.1:8000/docs
```

### ReDoc

```text
http://127.0.0.1:8000/redoc
```

The documentation allows you to view the available endpoints, parameters, data models, and test requests directly from the browser.

---

## 📂 Project Structure

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

## 🧠 Concepts Applied

This project was developed as part of my learning journey in **Python and Backend development**.

Throughout the development process, I practiced:

* REST API development
* FastAPI
* Pydantic
* SQLAlchemy ORM
* SQLite
* CRUD operations
* HTTP methods
* Dependency Injection with `Depends`
* HTTP Basic Authentication
* Pagination
* Data validation
* Exception handling
* Database session management
* Poetry
* Backend application organization

---

## 🔮 Future Improvements

Planned improvements for the project include:

* [ ] JWT authentication
* [ ] User registration and management
* [ ] Password hashing
* [ ] Task filtering
* [ ] Result sorting
* [ ] Search by task name
* [ ] Automated tests with Pytest
* [ ] Separation into layers (`routers`, `models`, `schemas`, `services`)
* [ ] Docker
* [ ] API deployment

---

## 👨‍💻 Author

### Guilherme Muniz

Developer in training focused on **Python Backend development**, API development, and web applications.

📧 **Email:** [muniz_157@outlook.com](mailto:muniz_157@outlook.com)

💻 **GitHub:** [NewEraM](https://github.com/NewEraM)

🔗 **LinkedIn:** [Guilherme Muniz | LinkedIn](https://linkedin.com/in/guilherme-muniz-8188a024/)

---

## 🌎 Language

<p align="center">
  <a href="README.md">🇧🇷 Português</a> |
  🇺🇸 <strong>English</strong>
</p>

---

## ⭐ Feedback

This project is part of my journey in learning **Python and Backend development**.

Feedback, suggestions, and contributions are always welcome!
