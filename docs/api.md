# Documentação das Rotas — Catálogo de Jogos

## 1. Visão Geral

O sistema expõe rotas HTTP para operações CRUD de jogos utilizando o padrão **Web MPA (Multi-Page Application)** com renderização server-side. As rotas `POST` retornam redirecionamentos (HTTP 303) seguindo o padrão **PRG (Post/Redirect/Get)** para evitar reenvio de formulários.

Todas as rotas que recebem dados de formulário utilizam `Content-Type: application/x-www-form-urlencoded`.

**URL Base:** `http://localhost:8000`

---

## 2. Tabela de Rotas

| Método | Endpoint                    | Descrição                           |
|--------|-----------------------------|-------------------------------------|
| GET    | `/`                         | Redireciona para `/jogos`           |
| GET    | `/jogos`                    | Lista todos os jogos                |
| GET    | `/jogos/novo`               | Exibe formulário de novo jogo       |
| POST   | `/jogos`                    | Cria um novo jogo                   |
| GET    | `/jogos/{jogo_id}/editar`   | Exibe formulário de edição          |
| POST   | `/jogos/{jogo_id}/editar`   | Atualiza um jogo existente          |
| POST   | `/jogos/{jogo_id}/excluir`  | Remove um jogo                      |

---

## 3. Detalhamento das Rotas

---

### `GET /`

Redireciona o usuário para a listagem de jogos.

- **Resposta:** `302 Redirect → /jogos`

---

### `GET /jogos`

Lista todos os jogos cadastrados no banco de dados.

- **Resposta:** `200 OK` — renderiza `lista.html`
- **Dados passados ao template:**
  - `jogos`: lista de objetos `Jogos` com o relacionamento `genero` carregado.

---

### `GET /jogos/novo`

Exibe o formulário para cadastro de um novo jogo.

- **Resposta:** `200 OK` — renderiza `form.html`
- **Dados passados ao template:**
  - `jogo`: `None` (indica criação)
  - `generos`: lista de todos os objetos `Genero` disponíveis

---

### `POST /jogos`

Cria um novo jogo com os dados enviados pelo formulário.

**Parâmetros do formulário (Form Data):**

| Campo      | Tipo    | Obrigatório | Descrição |
|------------|---------|-------------|-----------|
| `titulo`   | string  | Sim         | Título do jogo |
| `produtor` | string  | Sim         | Estúdio ou empresa desenvolvedora |
| `ano`      | integer | Sim         | Ano de lançamento |
| `genero_id`| integer | Sim         | ID do gênero (selecionado da lista) |
| `nota`     | float   | Não         | Nota de 0.0 a 10.0 (padrão: `0`) |
| `jogado`   | boolean | Não         | Se o jogo foi jogado (padrão: `False`) |

- **Resposta de sucesso:** `303 Redirect → /jogos`

---

### `GET /jogos/{jogo_id}/editar`

Exibe o formulário de edição preenchido com os dados do jogo.

**Parâmetros de path:**

| Parâmetro | Tipo    | Descrição |
|-----------|---------|-----------|
| `jogo_id` | integer | ID do jogo a ser editado |

- **Resposta:** `200 OK` — renderiza `form.html`
- **Dados passados ao template:**
  - `jogo`: objeto `Jogos` com os dados atuais
  - `generos`: lista de todos os objetos `Genero` disponíveis

---

### `POST /jogos/{jogo_id}/editar`

Atualiza os dados de um jogo existente.

**Parâmetros de path:**

| Parâmetro | Tipo    | Descrição |
|-----------|---------|-----------|
| `jogo_id` | integer | ID do jogo a ser atualizado |

**Parâmetros do formulário (Form Data):** idênticos ao `POST /jogos`.

- **Resposta de sucesso:** `303 Redirect → /jogos`

---

### `POST /jogos/{jogo_id}/excluir`

Remove permanentemente um jogo do banco de dados.

**Parâmetros de path:**

| Parâmetro | Tipo    | Descrição |
|-----------|---------|-----------|
| `jogo_id` | integer | ID do jogo a ser removido |

- **Resposta de sucesso:** `303 Redirect → /jogos`

---

## 4. Documentação Automática (Swagger)

O FastAPI gera documentação interativa automaticamente, acessível durante o desenvolvimento:

- **Swagger UI:** `http://localhost:8000/docs`
- **ReDoc:** `http://localhost:8000/redoc`
- **OpenAPI JSON:** `http://localhost:8000/openapi.json`

> As rotas que utilizam formulários HTML (`Form(...)`) podem apresentar comportamento diferente do esperado na UI do Swagger, pois o padrão esperado é `multipart/form-data` ou `application/x-www-form-urlencoded`, não `application/json`.

---

## 5. Arquivos Estáticos

| Caminho         | Endpoint montado | Descrição |
|-----------------|------------------|-----------|
| `static/`       | `/static`        | Arquivos CSS, imagens e outros recursos estáticos |
| `static/style.css` | `/static/style.css` | Folha de estilos principal da aplicação |
