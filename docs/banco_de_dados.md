# Banco de Dados — Catálogo de Jogos

## 1. Visão Geral

O sistema utiliza **PostgreSQL** como banco de dados relacional, hospedado na plataforma **Supabase**. A conexão é configurada via variável de ambiente `DATABASE_URL` e gerenciada pelo **SQLAlchemy 2.x** com sua API de mapeamento declarativo moderno (`Mapped` / `mapped_column`).

As tabelas são criadas automaticamente na inicialização da aplicação através do comando:

```python
Base.metadata.create_all(bind=engine)
```

---

## 2. Diagrama Entidade-Relacionamento (DER)

```
┌──────────────────┐          ┌──────────────────────────────┐
│     generos      │          │           jogos              │
├──────────────────┤          ├──────────────────────────────┤
│ id       INTEGER │◄────┐    │ id         INTEGER (PK)      │
│ nome     VARCHAR │     └────│ genero_id  INTEGER (FK)      │
└──────────────────┘          │ titulo     VARCHAR           │
                              │ produtor   VARCHAR           │
                              │ ano        INTEGER           │
                              │ nota       FLOAT             │
                              │ jogado     BOOLEAN           │
                              └──────────────────────────────┘
```

**Cardinalidade:** Um gênero pode estar associado a muitos jogos (1:N).

---

## 3. Descrição das Tabelas

### 3.1 Tabela `generos`

Armazena as categorias de gênero disponíveis para classificar os jogos.

| Coluna | Tipo    | Restrição   | Descrição               |
|--------|---------|-------------|-------------------------|
| `id`   | INTEGER | PRIMARY KEY | Identificador único auto-incrementado |
| `nome` | VARCHAR | NOT NULL    | Nome do gênero (ex: Aventura, RPG, Simulação) |

> **Nota:** Os registros desta tabela são inseridos manualmente no banco de dados. Não há interface web para gerenciamento de gêneros na versão atual.

---

### 3.2 Tabela `jogos`

Tabela principal do sistema. Armazena todos os jogos cadastrados pelos usuários.

| Coluna      | Tipo    | Restrição             | Descrição |
|-------------|---------|-----------------------|-----------|
| `id`        | INTEGER | PRIMARY KEY           | Identificador único auto-incrementado |
| `titulo`    | VARCHAR | NOT NULL              | Título do jogo |
| `produtor`  | VARCHAR | NOT NULL              | Empresa ou estúdio desenvolvedor |
| `ano`       | INTEGER | NOT NULL              | Ano de lançamento do jogo |
| `genero_id` | INTEGER | FOREIGN KEY → generos | Referência ao gênero do jogo |
| `nota`      | FLOAT   | DEFAULT 0             | Avaliação pessoal do usuário (0.0 a 10.0) |
| `jogado`    | BOOLEAN | DEFAULT FALSE         | Indica se o usuário já jogou o título |

---

## 4. Modelos ORM (SQLAlchemy)

```python
# models.py

class Genero(Base):
    __tablename__ = "generos"
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str]
    jogos: Mapped[list["Jogos"]] = relationship(back_populates="genero")


class Jogos(Base):
    __tablename__ = "jogos"
    id: Mapped[int] = mapped_column(primary_key=True)
    titulo: Mapped[str]
    produtor: Mapped[str]
    ano: Mapped[int]
    genero_id: Mapped[int] = mapped_column(ForeignKey("generos.id"))
    genero: Mapped["Genero"] = relationship(back_populates="jogos")
    nota: Mapped[float] = mapped_column(default=0)
    jogado: Mapped[bool] = mapped_column(default=False)
```

---

## 5. Configuração da Conexão

A conexão com o banco é configurada em `database.py` via `pydantic-settings`, que lê automaticamente o arquivo `.env`:

```python
class Settings(BaseSettings):
    DATABASE_URL: str
    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()
engine = create_engine(settings.DATABASE_URL)
```

**Formato da variável no `.env`:**

```env
DATABASE_URL=postgresql+psycopg://usuario:senha@host:porta/nome_do_banco
```

---

## 6. Gerenciamento de Sessões

A sessão do banco de dados é injetada nas rotas via dependência do FastAPI:

```python
def get_session():
    with Session(engine) as session:
        yield session
```

Isso garante que cada requisição receba uma sessão isolada e que ela seja encerrada corretamente ao final, mesmo em caso de exceções.

---

## 7. Exemplo de Dados

### Tabela `generos`

| id | nome         |
|----|--------------|
| 1  | Aventura     |
| 2  | RPG de Ação  |
| 3  | Simulação    |
| 4  | Roguelike    |

### Tabela `jogos`

| id | titulo                        | produtor         | ano  | genero_id | nota | jogado |
|----|-------------------------------|------------------|------|-----------|------|--------|
| 1  | The Legend of Zelda: TotK     | Nintendo         | 2023 | 1         | 9.8  | true   |
| 2  | Elden Ring                    | FromSoftware     | 2022 | 2         | 9.5  | false  |
| 3  | Stardew Valley                | ConcernedApe     | 2016 | 3         | 9.0  | true   |
| 4  | Hades                         | Supergiant Games | 2020 | 4         | 9.2  | false  |
