# models.py
from sqlalchemy.orm import Mapped, mapped_column
from database import Base


class Jogos(Base):
    __tablename__ = "jogos"

    id: Mapped[int] = mapped_column(primary_key=True)  # chave primária
    titulo: Mapped[str]  # obrigatório
    produtor: Mapped[str]
    ano: Mapped[int]
    genero: Mapped[str]  # por enquanto, texto
    nota: Mapped[float] = mapped_column(default=0)  # 0 a 10
    jogado: Mapped[bool] = mapped_column(default=False)
