from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI, Form, Request
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy import select
from sqlalchemy.orm import Session

from starlette.middleware.sessions import SessionMiddleware

import models
from database import Base, engine, get_session


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(lifespan=lifespan)

app.add_middleware(
    SessionMiddleware,
    secret_key="TESTE"
)

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

    flash = request.session.pop("flash", None)
    
    return templates.TemplateResponse(
        request,
        "lista.html",
        {"jogos": jogos,
            "flash":flash},
    )


# FORMULÁRIO DE NOVO JOGO
@app.get("/jogos/novo")
def form_novo(request: Request, session: Session = Depends(get_session)):
    generos = session.scalars(select(models.Genero)).all()
    return templates.TemplateResponse(
        request, "form.html", {"jogo": None, "generos": generos}
    )


@app.post("/jogos")
def criar(
    request: Request,
    titulo: str = Form(...),
    produtor: str = Form(...),
    ano: int = Form(...),
    genero_id: int = Form(...),  # agora recebe o id do gênero
    nota: float = Form(0),
    jogado: bool = Form(False),
    session: Session = Depends(get_session),
):

    jogo = models.Jogos(
        titulo=titulo,
        produtor=produtor,
        ano=ano,
        genero_id=genero_id,
        nota=nota,
        jogado=jogado,
    )

    jogo_existente = session.query(models.Jogos).filter_by(titulo=titulo,ano=ano,produtor=produtor).first()
    
    
    if jogo_existente:
        for i in range(0,100):
            print(i)
        request.session["flash"] = {
            "categoria": "error",
            "mensagem": "Esse jogo já existe.",
            "color":"Red"}
        
        return RedirectResponse(url="/jogos", status_code=303)
            
        
        
    elif not jogo_existente:
     session.add(jogo)
     session.commit()
     request.session["flash"] = {
            "categoria": "success",
            "mensagem": "Jogo cadastrado com sucesso!",
            "color" : "Green"
        }
     return RedirectResponse(url="/jogos", status_code=303)


# UPDATE — formulário de edição
@app.get("/jogos/{jogo_id}/editar")
def form_editar(
    jogo_id: int, request: Request, session: Session = Depends(get_session)
):
    jogo = session.get(models.Jogos, jogo_id)
    generos = session.scalars(select(models.Genero)).all()  # lista p/ o <select>
    return templates.TemplateResponse(
        request, "form.html", {"jogo": jogo, "generos": generos}
    )


@app.post("/jogos/{jogo_id}/editar")
def atualizar(
    jogo_id: int,
    titulo: str = Form(...),
    produtor: str = Form(...),
    ano: int = Form(...),
    genero_id: int = Form(...),  # agora recebe o id do gênero
    nota: float = Form(0),
    jogado: bool = Form(False),
    session: Session = Depends(get_session),
):
    jogo = session.get(models.Jogos, jogo_id)
    jogo.titulo, jogo.produtor, jogo.ano = titulo, produtor, ano
    jogo.genero_id, jogo.nota, jogo.jogado = genero_id, nota, jogado
    session.commit()
    return RedirectResponse(url="/jogos", status_code=303)


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
