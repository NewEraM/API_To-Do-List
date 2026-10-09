# API de Tarefas — To-Do List

<p align="right">
  🇧🇷 Português | <a href="./README.en.md">🇺🇸 English</a>
</p>

**Backend Python | FastAPI | SQLAlchemy | SQLite | Poetry | Docker**

API REST desenvolvida com Python e FastAPI para gerenciamento de tarefas. O projeto utiliza SQLAlchemy para persistência de dados no SQLite, Pydantic para validação de dados e autenticação HTTP Basic para proteger os endpoints.

## Tecnologias utilizadas

* Python
* FastAPI
* SQLAlchemy (ORM)
* SQLite
* Pydantic
* Poetry
* Docker e Docker Compose

## Funcionalidades

* Criar tarefas.
* Listar tarefas com paginação.
* Consultar tarefas pelo ID.
* Atualizar tarefas existentes.
* Excluir tarefas.
* Validar dados de entrada.
* Impedir tarefas com nomes duplicados.
* Proteger endpoints com autenticação HTTP Basic.
* Persistir dados em banco SQLite.

## Estrutura do projeto

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

*Adapte a estrutura acima aos arquivos existentes no repositório.*

## Pré-requisitos

* Git
* Docker com suporte ao Docker Compose

Alternativamente, você pode utilizar Podman com um provedor compatível com Compose.

## Como clonar o projeto

```bash
git clone https://github.com/NewEraM/API_To-Do-List.git
cd API_To-Do-List
```

## Variáveis de ambiente

Configure um arquivo `.env` conforme o exemplo abaixo, caso o Compose esteja configurado para carregá-lo:

```env
DATABASE_URL=sqlite:////app/tarefas.db
USER=admin
PASSWORD=senha_segura
```

**Importante:** ajuste o caminho do SQLite de acordo com o diretório de trabalho e os volumes configurados no container. Não compartilhe suas credenciais reais nem envie o arquivo `.env` ao GitHub.

## Executando com Docker

Na raiz do projeto, execute:

```bash
docker-compose up --build -d
```

Ou, com a versão integrada do Compose:

```bash
docker compose up --build -d
```

O comando constrói a imagem, instala as dependências conforme o Dockerfile e inicia a aplicação em segundo plano.

## Executando com Podman

Com a máquina do Podman iniciada, execute:

```bash
podman compose up --build -d
```

Esse comando exige um provedor Compose compatível instalado e configurado.

## Acessando a documentação

Se a porta `8000` estiver publicada no Compose, acesse:

* **Swagger UI:** http://localhost:8000/docs
* **ReDoc:** http://localhost:8000/redoc

Os endpoints protegidos exigem as credenciais definidas nas variáveis `USER` e `PASSWORD`.

## Endpoints

| Método | Endpoint                         | Descrição                   |
| ------ | -------------------------------- | --------------------------- |
| GET    | `/tarefas`                       | Lista tarefas com paginação |
| GET    | `/tarefas/{id_tarefa}`           | Consulta uma tarefa pelo ID |
| POST   | `/adcionar_tarefas`              | Cria uma tarefa             |
| PUT    | `/atualizar_tarefas/{id_tarefa}` | Atualiza uma tarefa         |
| DELETE | `/deletar_tarefas/{id_tarefa}`   | Exclui uma tarefa           |

## Exemplo de criação de tarefa

Envie uma requisição `POST` para `/adcionar_tarefas` com o seguinte JSON:

```json
{
  "nome_tarefa": "Estudar FastAPI",
  "descricao_tarefa": "Praticar desenvolvimento de APIs REST",
  "status_tarefa": false
}
```

## Paginação

Para listar a primeira página com até 10 tarefas:

```http
GET /tarefas?page=1&limit=10
```

## Desenvolvimento

O Docker Compose pode sincronizar os arquivos locais com o container por meio de volumes. Com o servidor configurado para observar alterações, as mudanças no código podem ser aplicadas automaticamente durante o desenvolvimento.

## Comandos úteis

Consultar os containers:

```bash
docker-compose ps
```

Visualizar os logs:

```bash
docker-compose logs -f
```

Parar e remover os containers e a rede:

```bash
docker-compose down
```

Com Podman:

```bash
podman compose logs -f
podman compose down
```

A persistência do banco depende da configuração dos volumes. Verifique onde o arquivo SQLite está armazenado antes de remover volumes.

## Execução local com Poetry

Se Python e Poetry estiverem instalados, execute:

```bash
poetry install
```

Configure as variáveis de ambiente e inicie a aplicação. Se o arquivo for `ToDoList.py`, o comando poderá ser:

```bash
poetry run uvicorn ToDoList:app --reload
```

## Objetivo do projeto

Este projeto faz parte da minha evolução como desenvolvedor Backend Python e demonstra conhecimentos práticos em APIs REST, operações CRUD, validação de dados, autenticação, paginação, ORM, persistência de dados e conteinerização.

## Desenvolvedor

**Guilherme Muniz**

* GitHub: [NewEraM](https://github.com/NewEraM)
* Portfólio: [Guilherme Muniz | Backend Python](https://neweram.github.io/)
* LinkedIn: [Guilherme Muniz](https://www.linkedin.com/in/guilherme-muniz-8188a0247/)
