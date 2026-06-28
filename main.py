from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI, Form, Request
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy import select
from sqlalchemy.orm import Session

import models
from database import Base, engine, get_session


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(lifespan=lifespan)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


# Página inicial
@app.get("/")
def home():
    return RedirectResponse(url="/jogos")


# LISTAR
@app.get("/jogos")
def listar(request: Request, session: Session = Depends(get_session)):
    jogos = session.scalars(select(models.Jogos)).all()
    return templates.TemplateResponse(
        request,
        "lista.html",
        {"jogos": jogos},
    )


# FORMULÁRIO DE NOVO JOGO
@app.get("/jogos/novo")
def form_novo(request: Request):
    return templates.TemplateResponse(
        request,
        "form.html",
        {"jogo": None},
    )


# CRIAR JOGO
@app.post("/jogos")
def criar(
    titulo: str = Form(...),
    produtor: str = Form(...),
    ano: int = Form(...),
    genero: str = Form(...),
    nota: float = Form(0),
    jogado: bool = Form(False),
    session: Session = Depends(get_session),
):
    jogo = models.Jogos(
        titulo=titulo,
        produtor=produtor,
        ano=ano,
        genero=genero,
        nota=nota,
        jogado=jogado,
    )

    session.add(jogo)
    session.commit()

    return RedirectResponse(
        url="/jogos",
        status_code=303,
    )


# UPDATE — formulário de edição
@app.get("/jogos/{jogo_id}/editar")
def form_editar(
    jogo_id: int,
    request: Request,
    session: Session = Depends(get_session),
):
    jogo = session.get(models.Jogos, jogo_id)
    return templates.TemplateResponse(
        request,
        "form.html",
        {"jogo": jogo},
    )


# UPDATE — salva as alterações
@app.post("/jogos/{jogo_id}/editar")
def atualizar(
    jogo_id: int,
    titulo: str = Form(...),
    produtor: str = Form(...),
    ano: int = Form(...),
    genero: str = Form(...),
    nota: float = Form(0),
    jogado: bool = Form(False),
    session: Session = Depends(get_session),
):
    jogo = session.get(models.Jogos, jogo_id)

    jogo.titulo = titulo
    jogo.produtor = produtor
    jogo.ano = ano
    jogo.genero = genero
    jogo.nota = nota
    jogo.jogado = jogado

    session.commit()

    return RedirectResponse(
        url="/jogos",
        status_code=303,
    )


# DELETE — remove do banco
@app.post("/jogos/{jogo_id}/excluir")
def excluir(
    jogo_id: int,
    session: Session = Depends(get_session),
):
    jogo = session.get(models.Jogos, jogo_id)

    session.delete(jogo)
    session.commit()

    return RedirectResponse(
        url="/jogos",
        status_code=303,
    )
