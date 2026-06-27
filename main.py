from contextlib import asynccontextmanager
from fastapi import FastAPI

import models                         # importa os modelos p/ registrá-los no Base
from database import Base, engine

@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)   # cria as tabelas no Supabase
    yield                                    # (executa uma vez, ao iniciar)

app = FastAPI(lifespan=lifespan)
