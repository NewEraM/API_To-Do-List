from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic import BaseModel, ConfigDict
from typing import Optional
import secrets
import os
from dotenv import load_dotenv

load_dotenv()  # Carrega as variáveis de ambiente do arquivo .env

from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker, Session

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

app = FastAPI(
    title="API de Tarefas modelo To-Do",
    description="API feita para gerenciar tarefas",
    version="1.0.0",
    contact={
        "name": "Guilherme Muniz",
        "email": "muniz_157@outlook.com",
    },
)

USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")
security = HTTPBasic()


class TarefasDB(Base):
    __tablename__ = "Tarefas"

    id = Column(Integer, primary_key=True, index=True)
    nome_tarefa = Column(String, nullable=False, index=True)
    descricao_tarefa = Column(String, nullable=False, index=True)
    status_tarefa = Column(Boolean, default=False, nullable=False)


class TarefaCreate(BaseModel):
    nome_tarefa: str
    descricao_tarefa: str
    status_tarefa: bool = False


class TarefaUpdate(BaseModel):
    nome_tarefa: Optional[str] = None
    descricao_tarefa: Optional[str] = None
    status_tarefa: Optional[bool] = None


class TarefaResposta(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    nome_tarefa: str
    descricao_tarefa: str
    status_tarefa: bool


Base.metadata.create_all(bind=engine)


def sessao_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def autenticar_user(credentials: HTTPBasicCredentials = Depends(security)):
    is_username_correct = secrets.compare_digest(credentials.username, USER)
    is_password_correct = secrets.compare_digest(credentials.password, PASSWORD)

    if not (is_username_correct and is_password_correct):
        raise HTTPException(
            status_code=401,
            detail="Usuario ou senha invalidos",
            headers={"WWW-Authenticate": "Basic"},
        )


@app.get("/tarefas")
def get_tarefas(
    page: int = 1,
    limit: int = 10,
    db: Session = Depends(sessao_db),
    credentials: HTTPBasicCredentials = Depends(autenticar_user),
):
    if page < 1 or limit < 1:
        raise HTTPException(
            status_code=400,
            detail="Page ou limit estao com valores invalidos",
        )

    tarefas = db.query(TarefasDB).offset((page - 1) * limit).limit(limit).all()

    if not tarefas:
        return {"message": "Nao possui nenhuma tarefa"}

    total_tarefas = db.query(TarefasDB).count()

    return {
        "page": page,
        "limit": limit,
        "total": total_tarefas,
        "tarefas": [
            {
                "id": tarefa.id,
                "nome_tarefa": tarefa.nome_tarefa,
                "descricao_tarefa": tarefa.descricao_tarefa,
                "status_tarefa": tarefa.status_tarefa,
            }
            for tarefa in tarefas
        ],
    }


@app.get("/tarefas/{id_tarefa}")
def get_tarefa_por_id(
    id_tarefa: int,
    db: Session = Depends(sessao_db),
    credentials: HTTPBasicCredentials = Depends(autenticar_user),
):
    tarefa = db.query(TarefasDB).filter(TarefasDB.id == id_tarefa).first()

    if not tarefa:
        raise HTTPException(status_code=404, detail="Tarefa nao encontrada")

    return TarefaResposta.model_validate(tarefa)


@app.post("/adicionar_tarefas")
def post_tarefa(
    tarefa: TarefaCreate,
    db: Session = Depends(sessao_db),
    credentials: HTTPBasicCredentials = Depends(autenticar_user),
):
    tarefa_existente = (
        db.query(TarefasDB)
        .filter(TarefasDB.nome_tarefa == tarefa.nome_tarefa)
        .first()
    )

    if tarefa_existente:
        raise HTTPException(status_code=400, detail="Essa tarefa ja existe no banco de dados")

    nova_tarefa = TarefasDB(
        nome_tarefa=tarefa.nome_tarefa,
        descricao_tarefa=tarefa.descricao_tarefa,
        status_tarefa=tarefa.status_tarefa,
    )
    db.add(nova_tarefa)
    db.commit()
    db.refresh(nova_tarefa)

    return {"message": "A tarefa foi criada com sucesso!"}


@app.put("/atualizar_tarefas/{id_tarefa}")
def put_tarefa(
    id_tarefa: int,
    tarefa: TarefaUpdate,
    db: Session = Depends(sessao_db),
    credentials: HTTPBasicCredentials = Depends(autenticar_user),
):
    tarefa_db = db.query(TarefasDB).filter(TarefasDB.id == id_tarefa).first()

    if not tarefa_db:
        raise HTTPException(status_code=404, detail="Essa tarefa nao foi encontrada")

    if tarefa.nome_tarefa is not None:
        tarefa_db.nome_tarefa = tarefa.nome_tarefa
    if tarefa.descricao_tarefa is not None:
        tarefa_db.descricao_tarefa = tarefa.descricao_tarefa
    if tarefa.status_tarefa is not None:
        tarefa_db.status_tarefa = tarefa.status_tarefa

    db.commit()
    db.refresh(tarefa_db)

    return {"message": "A tarefa foi atualizada com sucesso!"}


@app.delete("/deletar_tarefas/{id_tarefa}")
def delete_tarefa(
    id_tarefa: int,
    db: Session = Depends(sessao_db),
    credentials: HTTPBasicCredentials = Depends(autenticar_user),
):
    tarefa_db = db.query(TarefasDB).filter(TarefasDB.id == id_tarefa).first()

    if not tarefa_db:
        raise HTTPException(status_code=404, detail="Essa tarefa nao foi encontrada")

    db.delete(tarefa_db)
    db.commit()

    return {"message": "A tarefa foi deletada com sucesso!"}
