# To-Do List API

<p align="right">
  <a href="./README.md">🇧🇷 Português</a> | 🇺🇸 English
</p>

**Python Backend | FastAPI | SQLAlchemy | SQLite | Poetry | Docker**

A REST API built with Python and FastAPI for task management. The project uses SQLAlchemy for SQLite persistence, Pydantic for data validation, and HTTP Basic authentication to protect its endpoints.

## Technologies

* Python
* FastAPI
* SQLAlchemy (ORM)
* SQLite
* Pydantic
* Poetry
* Docker and Docker Compose

## Features

* Create tasks.
* List tasks with pagination.
* Retrieve tasks by ID.
* Update existing tasks.
* Delete tasks.
* Validate input data.
* Prevent duplicate task names.
* Protect endpoints with HTTP Basic authentication.
* Persist data in an SQLite database.

## Project structure

```text
API_To-Do-List/
├── Dockerfile
├── docker-compose.yml
├── pyproject.toml
├── poetry.lock
├── .env
├── .dockerignore
├── README.md
├── README.en.md
└── ToDoList.py
```

*Adjust this example to match the actual files in your repository.*

## Prerequisites

* Git
* Docker with Docker Compose support

Alternatively, you can use Podman with a compatible Compose provider.

## Clone the repository

```bash
git clone https://github.com/NewEraM/API_To-Do-List.git
cd API_To-Do-List
```

## Environment variables

Create a `.env` file like the example below, if your Compose configuration loads this file:

```env
DATABASE_URL=sqlite:////app/tarefas.db
USER=admin
PASSWORD=your_secure_password
```

**Important:** adjust the SQLite path to match the container's working directory and volume configuration. Do not share real credentials or commit your `.env` file to GitHub.

## Run with Docker

From the project root, execute:

```bash
docker-compose up --build -d
```

Alternatively, use the integrated Compose command:

```bash
docker compose up --build -d
```

This command builds the image, installs dependencies as configured in the Dockerfile, and starts the application in the background.

## Run with Podman

Make sure your Podman machine is running, then execute:

```bash
podman compose up --build -d
```

This command requires a compatible Compose provider to be installed and configured.

## Access the API documentation

If port `8000` is published in your Compose configuration, open:

* **Swagger UI:** http://localhost:8000/docs
* **ReDoc:** http://localhost:8000/redoc

Protected endpoints require the credentials configured through the `USER` and `PASSWORD` environment variables.

## Endpoints

| Method | Endpoint                         | Description                 |
| ------ | -------------------------------- | --------------------------- |
| GET    | `/tarefas`                       | Lists tasks with pagination |
| GET    | `/tarefas/{id_tarefa}`           | Retrieves a task by ID      |
| POST   | `/adcionar_tarefas`              | Creates a task              |
| PUT    | `/atualizar_tarefas/{id_tarefa}` | Updates a task              |
| DELETE | `/deletar_tarefas/{id_tarefa}`   | Deletes a task              |

## Create a task

Send a `POST` request to `/adcionar_tarefas` with the following JSON body:

```json
{
  "nome_tarefa": "Study FastAPI",
  "descricao_tarefa": "Practice REST API development",
  "status_tarefa": false
}
```

## Pagination

To retrieve the first page with up to 10 tasks:

```http
GET /tarefas?page=1&limit=10
```

## Development

Docker Compose can synchronize local files with the container using volumes. When the application server is configured to watch for file changes, code updates can be applied automatically during development.

## Useful commands

List running containers:

```bash
docker-compose ps
```

Follow application logs:

```bash
docker-compose logs -f
```

Stop and remove the containers and network:

```bash
docker-compose down
```

With Podman:

```bash
podman compose logs -f
podman compose down
```

Database persistence depends on the volume configuration. Check where the SQLite database is stored before removing volumes.

## Run locally with Poetry

If Python and Poetry are installed, run:

```bash
poetry install
```

Configure the environment variables and start the application. If the module is named `ToDoList.py`, the command may be:

```bash
poetry run uvicorn ToDoList:app --reload
```

## Project purpose

This project is part of my journey as a Python Backend Developer and demonstrates practical knowledge of REST APIs, CRUD operations, data validation, authentication, pagination, ORM, database persistence, and containerization.

## Developer

**Guilherme Muniz**

* GitHub: [NewEraM](https://github.com/NewEraM)
* Portfolio: [Guilherme Muniz | Backend Python](https://neweram.github.io/)
* LinkedIn: [Guilherme Muniz](https://www.linkedin.com/in/guilherme-muniz-8188a0247/)
