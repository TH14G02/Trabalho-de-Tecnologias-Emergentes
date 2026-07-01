# Arquitetura do Sistema — Catálogo de Jogos

## 1. Visão Geral da Arquitetura

O sistema segue o padrão **MVC (Model-View-Controller)** adaptado para o ecossistema FastAPI, onde:

- **Model** → `models.py` (entidades ORM com SQLAlchemy)
- **View** → `templates/` (HTML renderizado com Jinja2)
- **Controller** → `main.py` (rotas e lógica de negócio)

A persistência é feita em um banco de dados **PostgreSQL** hospedado no **Supabase** (nuvem), e a configuração de conexão é gerenciada via variáveis de ambiente com `pydantic-settings`.

---

## 2. Diagrama de Camadas

```
┌─────────────────────────────────────────────────────┐
│                    Cliente (Browser)                │
└───────────────────────┬─────────────────────────────┘
                        │ HTTP (GET / POST)
┌───────────────────────▼─────────────────────────────┐
│              FastAPI (main.py)                      │
│  ┌─────────────┐  ┌──────────────┐  ┌────────────┐  │
│  │   Rotas     │  │  Jinja2      │  │  Arquivos  │  │
│  │  (CRUD)     │  │  Templates   │  │  Estáticos │  │
│  └──────┬──────┘  └──────────────┘  └────────────┘  │
│         │                                            │
│  ┌──────▼──────────────────────────┐                │
│  │   SQLAlchemy ORM (models.py)    │                │
│  └──────────────────────────────┬──┘                │
└─────────────────────────────────┼───────────────────┘
                                  │ SQL
┌─────────────────────────────────▼───────────────────┐
│         PostgreSQL — Supabase (nuvem)               │
└─────────────────────────────────────────────────────┘
```

---

## 3. Stack Tecnológica

| Camada         | Tecnologia              | Versão mínima | Função |
|----------------|-------------------------|---------------|--------|
| Backend        | FastAPI                 | 0.138.1       | Framework web ASGI |
| ORM            | SQLAlchemy              | 2.0.51        | Mapeamento objeto-relacional |
| Templates      | Jinja2                  | 3.1.6         | Renderização de HTML no servidor |
| Configuração   | pydantic-settings       | 2.14.2        | Leitura de variáveis de ambiente |
| Driver BD      | psycopg / psycopg2      | 3.3.4 / 2.9.12 | Conector PostgreSQL |
| Forms          | python-multipart        | 0.0.32        | Parse de formulários HTML |
| Banco de Dados | PostgreSQL (Supabase)   | —             | Persistência de dados |
| Runtime        | Python                  | 3.12+         | Linguagem base |

---

## 4. Estrutura de Diretórios

```
Trabalho-de-Tecnologias-Emergentes/
├── main.py              # Rotas da aplicação e bootstrap do FastAPI
├── models.py            # Modelos ORM (Jogos, Genero)
├── database.py          # Engine, Base e sessão do SQLAlchemy
├── pyproject.toml       # Dependências e tarefas (uv + taskipy)
├── .env                 # Variáveis de ambiente (DATABASE_URL) — não versionado
├── static/
│   └── style.css        # Estilos globais da aplicação
├── templates/
│   ├── base.html        # Layout base com header e hero section
│   ├── form.html        # Formulário de criação e edição de jogos
│   ├── lista.html       # Listagem de todos os jogos (grid de cards)
│   └── previewFinal.html # Preview estático da interface (apresentação)
└── docs/                # Documentação técnica do projeto
```

---

## 5. Fluxo de uma Requisição

1. O browser envia uma requisição HTTP para o servidor FastAPI.
2. O roteador do FastAPI identifica o endpoint correspondente em `main.py`.
3. O endpoint obtém uma sessão de banco de dados via `Depends(get_session)` (injeção de dependência).
4. A lógica de negócio é executada: leitura ou escrita via SQLAlchemy ORM usando os modelos de `models.py`.
5. Para rotas `GET`, o template Jinja2 correspondente é renderizado com os dados e retornado como HTML.
6. Para rotas `POST`, após a operação, o usuário é redirecionado com `RedirectResponse` (padrão PRG — Post/Redirect/Get).

---

## 6. Decisões de Projeto

| Decisão | Justificativa |
|---------|---------------|
| FastAPI como framework | Performance com ASGI, tipagem nativa com Pydantic, injeção de dependências embutida. |
| Renderização server-side (SSR) com Jinja2 | Simplicidade de implementação sem necessidade de frontend SPA separado. |
| Supabase como banco de dados | Banco PostgreSQL gerenciado na nuvem, eliminando necessidade de setup local. |
| SQLAlchemy 2.x com `Mapped` | API moderna e type-safe para definição de modelos ORM. |
| Padrão PRG nos formulários | Previne o reenvio de dados ao atualizar a página após um `POST`. |
| `uv` como gerenciador de pacotes | Gerenciador moderno e rápido, compatível com `pyproject.toml`. |
