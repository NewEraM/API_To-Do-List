# API de Tarefas — To-Do List

### Backend Python | FastAPI | SQLAlchemy | SQLite | Poetry | Docker

API REST desenvolvida em Python com FastAPI para gerenciamento de tarefas. O projeto utiliza SQLAlchemy para persistência de dados no SQLite, Pydantic para validação de dados e autenticação HTTP Basic para proteger os endpoints.

## Tecnologias utilizadas

* **Python** — linguagem de programação.
* **FastAPI** — criação de APIs REST.
* **SQLAlchemy** — mapeamento objeto-relacional (ORM).
* **SQLite** — banco de dados relacional.
* **Pydantic** — validação e estruturação de dados.
* **Poetry** — gerenciamento de dependências.
* **Docker / Docker Compose** — conteinerização e execução da aplicação.

## Funcionalidades

* Criar novas tarefas.
* Listar tarefas com paginação.
* Consultar uma tarefa pelo ID.
* Atualizar tarefas existentes.
* Excluir tarefas pelo ID.
* Validar dados de entrada.
* Impedir o cadastro de tarefas com nomes duplicados.
* Proteger os endpoints com autenticação HTTP Basic.
* Persistir os dados utilizando SQLite.

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
└── ToDoList.py
```

> A estrutura acima é uma sugestão. Ajuste os nomes dos arquivos conforme a organização real do seu repositório.

## Pré-requisitos

Para executar o projeto utilizando Docker, tenha instalado:

* [Git](https://git-scm.com/)
* [Docker](https://www.docker.com/) com suporte ao Docker Compose.

Se preferir utilizar Podman, instale o [Podman](https://podman.io/) e o suporte ao Compose correspondente.

## Como clonar o repositório

Abra o terminal e execute:

```bash
git clone https://github.com/NewEraM/API_To-Do-List.git
```

Entre na pasta do projeto:

```bash
cd API_To-Do-List
```

## Configuração das variáveis de ambiente

O projeto utiliza variáveis de ambiente para configurar a conexão com o banco de dados e as credenciais de autenticação.

Configure o arquivo `.env` conforme o exemplo abaixo, caso o seu `docker-compose.yml` utilize esse arquivo:

```env
DATABASE_URL=sqlite:////app/tarefas.db
USER=admin
PASSWORD=senha_segura
```

**Importante:** o caminho do banco de dados deve corresponder ao caminho utilizado dentro do container. Se o projeto usar outro diretório ou um volume específico para o SQLite, ajuste a variável `DATABASE_URL`.

Não compartilhe credenciais reais nem envie seu arquivo `.env` para o GitHub.

## Construindo e iniciando a aplicação

Na raiz do projeto, execute:

```bash
docker-compose up --build -d
```

Esse comando:

1. Constrói a imagem utilizando o `Dockerfile`.
2. Instala as dependências definidas no projeto com Poetry, conforme configurado no Dockerfile.
3. Cria e inicia o container da aplicação em segundo plano.
4. Disponibiliza a API na porta configurada no `docker-compose.yml`.

Se estiver utilizando uma versão do Docker Compose que utiliza o comando integrado ao Docker CLI, você também pode executar:

```bash
docker compose up --build -d
```

### Executando com Podman

Caso utilize Podman no Windows, com a máquina do Podman iniciada, execute:

```bash
podman compose up --build -d
```

O comando depende de um provedor compatível com Compose instalado e configurado.

## Acessando a API

Após iniciar o container, abra a documentação interativa do FastAPI no navegador:

```text
http://localhost:8000/docs
```

A URL acima pressupõe que a porta `8000` esteja publicada no `docker-compose.yml`.

Você também pode acessar a documentação alternativa em:

```text
http://localhost:8000/redoc
```

Os endpoints protegidos exigem as credenciais configuradas nas variáveis `USER` e `PASSWORD`.

## Endpoints disponíveis

| Método | Endpoint                         | Descrição                   |
| ------ | -------------------------------- | --------------------------- |
| GET    | `/tarefas`                       | Lista tarefas com paginação |
| GET    | `/tarefas/{id_tarefa}`           | Consulta uma tarefa pelo ID |
| POST   | `/adcionar_tarefas`              | Cria uma tarefa             |
| PUT    | `/atualizar_tarefas/{id_tarefa}` | Atualiza uma tarefa         |
| DELETE | `/deletar_tarefas/{id_tarefa}`   | Exclui uma tarefa           |

### Exemplo de criação de tarefa

Envie uma requisição `POST` para `/adcionar_tarefas` com o seguinte JSON:

```json
{
  "nome_tarefa": "Estudar FastAPI",
  "descricao_tarefa": "Praticar desenvolvimento de APIs REST",
  "status_tarefa": false
}
```

### Exemplo de paginação

Para listar a primeira página com até 10 tarefas:

```text
GET /tarefas?page=1&limit=10
```

## Desenvolvimento com recarregamento automático

O `docker-compose.yml` pode utilizar um volume para sincronizar os arquivos locais com o container e executar a aplicação com recarregamento automático.

Assim, ao modificar o código Python, as alterações podem ser aplicadas sem precisar reconstruir a imagem a cada mudança, desde que o servidor esteja configurado para observar os arquivos.

## Verificando os logs

Para consultar os logs da aplicação:

```bash
docker-compose logs -f
```

Para verificar os containers em execução:

```bash
docker-compose ps
```

Para consultar os logs usando Podman Compose:

```bash
podman compose logs -f
```

## Parando a aplicação

Para parar e remover os containers e a rede criada pelo Compose, execute:

```bash
docker-compose down
```

Ou, utilizando a sintaxe integrada mais recente:

```bash
docker compose down
```

Com Podman:

```bash
podman compose down
```

Os dados persistentes dependem da configuração dos volumes. Antes de remover volumes, verifique onde o banco SQLite está armazenado para evitar perder dados.

## Executando localmente sem Docker

Se preferir executar o projeto diretamente na sua máquina, tenha Python e Poetry instalados.

Instale as dependências:

```bash
poetry install
```

Configure as variáveis de ambiente no arquivo `.env` e inicie a aplicação com o comando adequado ao nome do arquivo e à configuração do projeto. Por exemplo, se o módulo for `ToDoList.py`:

```bash
poetry run uvicorn ToDoList:app --reload
```

A documentação estará disponível em `http://localhost:8000/docs`.

## Objetivo do projeto

Este projeto faz parte da minha evolução como desenvolvedor Backend Python e demonstra a aplicação prática de conceitos como desenvolvimento de APIs REST, operações CRUD, validação de dados, autenticação, paginação, ORM, persistência de dados e conteinerização.

**Desenvolvido por Guilherme Muniz**

* GitHub: [NewEraM](https://github.com/NewEraM)
* Portfólio: [Guilherme Muniz | Backend Python](https://neweram.github.io/)
* LinkedIn: [Guilherme Muniz](https://www.linkedin.com/in/guilherme-muniz-8188a0247/)
