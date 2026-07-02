# models.py
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base


class Genero(Base):
    __tablename__ = "generos"
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str]
    jogos: Mapped[list["Jogos"]] = relationship(back_populates="genero")


class Jogos(Base):
    __tablename__ = "jogos"

    id: Mapped[int] = mapped_column(primary_key=True)  # chave primária
    titulo: Mapped[str]  # obrigatório
    produtor: Mapped[str]
    ano: Mapped[int]
    genero_id: Mapped[int] = mapped_column(ForeignKey("generos.id"))  # FK
    genero: Mapped["Genero"] = relationship(back_populates="jogos")
    nota: Mapped[float] = mapped_column(default=0)  # 0 a 10
    jogado: Mapped[bool] = mapped_column(default=False)
    imagem: Mapped[str] = mapped_column(nullable=True)