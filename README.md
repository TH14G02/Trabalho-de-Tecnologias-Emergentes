# Catálogo de Jogos

Aplicação web para gerenciamento de uma biblioteca pessoal de jogos. Desenvolvida como trabalho final da disciplina de **Tecnologias Emergentes** no **Instituto Federal do Piauí — Campus Piripiri**.

O sistema permite cadastrar, visualizar, editar e excluir jogos, com suporte a categorização por gênero, atribuição de notas e controle de status (jogado / não jogado).

---

## Tecnologias

| Camada      | Tecnologia                       |
|-------------|----------------------------------|
| Backend     | Python 3.12 + FastAPI            |
| ORM         | SQLAlchemy 2.x                   |
| Templates   | Jinja2 (Server-Side Rendering)   |
| Banco       | PostgreSQL via Supabase (nuvem)  |
| Config      | pydantic-settings + `.env`       |
| Pacotes     | uv                               |

---

## Funcionalidades

- Listagem de jogos em layout de cards
- Cadastro com título, produtor, ano, gênero, nota e status
- Edição de todos os campos
- Exclusão de jogos
- Interface responsiva com design temático (dark mode)

---

## Pré-requisitos

- Python 3.12+
- [uv](https://docs.astral.sh/uv/getting-started/installation/) instalado

---

## Instalação

```bash
# 1. Clone o repositório
git clone <url-do-repositorio>
cd Trabalho-de-Tecnologias-Emergentes

# 2. Instale as dependências
uv sync

# 3. Configure as variáveis de ambiente
# Crie um arquivo .env na raiz com o conteúdo:
# DATABASE_URL=postgresql+psycopg://usuario:senha@host:porta/banco
```

---

## Executando

```bash
uv run task run
```

Acesse em: **http://localhost:8000**

> Na primeira execução, as tabelas são criadas automaticamente. Lembre-se de popular a tabela `generos` antes de cadastrar jogos — consulte o [Manual do Usuário](docs/manual.md#34-popular-a-tabela-de-gêneros).

---

## Estrutura do Projeto

```
├── main.py              # Rotas e bootstrap da aplicação
├── models.py            # Modelos ORM (Jogos, Genero)
├── database.py          # Engine, Base e injeção de sessão
├── pyproject.toml       # Dependências e tarefas
├── .env                 # Variáveis de ambiente (não versionado)
├── static/
│   └── style.css        # Estilos da aplicação
├── templates/
│   ├── base.html        # Layout base
│   ├── form.html        # Formulário de criação e edição
│   └── lista.html       # Listagem de jogos
└── docs/                # Documentação técnica
    ├── requisitos.md
    ├── arquitetura.md
    ├── banco_de_dados.md
    ├── api.md
    ├── fluxo.md
    └── manual.md
```

---

## Tarefas

```bash
uv run task run     # Inicia o servidor de desenvolvimento
uv run task lint    # Verifica estilo de código (ruff)
uv run task format  # Formata o código (ruff)
```

---

## Documentação

A documentação completa do projeto está na pasta [`docs/`](docs/):

- [Requisitos](docs/requisitos.md) — Requisitos funcionais, não funcionais e regras de negócio
- [Arquitetura](docs/arquitetura.md) — Stack, diagrama de camadas e decisões de projeto
- [Banco de Dados](docs/banco_de_dados.md) — Modelagem, DER e descrição das tabelas
- [API / Rotas](docs/api.md) — Documentação de todas as rotas HTTP
- [Fluxo do Sistema](docs/fluxo.md) — Diagramas de fluxo das operações
- [Manual do Usuário](docs/manual.md) — Guia de instalação e uso

---

## Integrantes

> Insira aqui o nome dos integrantes do grupo.

---

*Instituto Federal do Piauí — Campus Piripiri · Tecnologias Emergentes · 2025*
