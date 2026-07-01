# Manual do Usuário — Catálogo de Jogos

## 1. Introdução

O **Catálogo de Jogos** é uma aplicação web para gerenciar sua biblioteca pessoal de jogos. Com ele você pode registrar os jogos que tem interesse, acompanhar quais já jogou, atribuir notas e organizá-los por gênero.

---

## 2. Requisitos para Execução

Antes de iniciar, certifique-se de ter instalado:

- **Python 3.12** ou superior
- **uv** (gerenciador de pacotes) — [instruções de instalação](https://docs.astral.sh/uv/getting-started/installation/)
- Acesso à internet (para conexão com o banco Supabase)

---

## 3. Instalação e Configuração

### 3.1 Clonar o repositório

```bash
git clone <url-do-repositorio>
cd Trabalho-de-Tecnologias-Emergentes
```

### 3.2 Instalar as dependências

```bash
uv sync
```

### 3.3 Configurar o arquivo `.env`

Crie um arquivo `.env` na raiz do projeto com a URL de conexão ao banco de dados:

```env
DATABASE_URL=postgresql+psycopg://usuario:senha@host:porta/nome_do_banco
```

> Substitua `usuario`, `senha`, `host`, `porta` e `nome_do_banco` pelos dados fornecidos pelo Supabase ou pelo administrador do banco.

### 3.4 Popular a tabela de gêneros

A tabela de gêneros deve ser populada manualmente no banco de dados antes do primeiro uso. Execute o SQL abaixo no seu cliente PostgreSQL ou pelo painel do Supabase:

```sql
INSERT INTO generos (nome) VALUES
  ('Ação'),
  ('Aventura'),
  ('RPG'),
  ('RPG de Ação'),
  ('Simulação'),
  ('Estratégia'),
  ('Esportes'),
  ('Roguelike'),
  ('Plataforma'),
  ('Puzzle');
```

---

## 4. Executando a Aplicação

### Modo de desenvolvimento (com hot-reload)

```bash
uv run task run
```

Ou diretamente:

```bash
uv run fastapi dev main.py
```

A aplicação estará disponível em: **http://localhost:8000**

---

## 5. Guia de Uso

### 5.1 Página Inicial — Listagem de Jogos

Ao acessar `http://localhost:8000`, você é redirecionado automaticamente para a lista de jogos.

A tela exibe todos os jogos cadastrados em um layout de cards, mostrando para cada jogo:
- 🎮 Ícone de jogo
- **Título** e informações de produtor e ano
- **Tag de gênero**
- **Nota** em destaque
- **Status** ("Jogado" ou "Não jogado")
- Botões de **Editar** e **Excluir**

---

### 5.2 Cadastrar um Novo Jogo

1. Clique no botão **`+ Novo jogo`** na barra de navegação ou na barra da seção.
2. Preencha os campos do formulário:
   - **Título** *(obrigatório)*: nome do jogo.
   - **Produtor** *(obrigatório)*: estúdio ou empresa responsável.
   - **Ano** *(obrigatório)*: ano de lançamento (número inteiro).
   - **Gênero** *(obrigatório)*: selecione na lista suspensa.
   - **Nota**: valor de `0` a `10`, com até uma casa decimal (ex: `9.5`). Padrão: `0`.
   - **Jogado**: marque o checkbox se você já jogou este título.
3. Clique em **Salvar**.

O jogo aparecerá na listagem imediatamente após o cadastro.

---

### 5.3 Editar um Jogo

1. Na listagem, localize o jogo que deseja editar.
2. Clique no botão **`Editar`** do card correspondente.
3. O formulário será aberto com os dados atuais preenchidos.
4. Faça as alterações desejadas e clique em **Salvar**.

---

### 5.4 Excluir um Jogo

1. Na listagem, localize o jogo que deseja remover.
2. Clique no botão **`Excluir`** do card correspondente.
3. A exclusão é imediata — o jogo será removido permanentemente do banco de dados.

> ⚠️ **Atenção:** a exclusão não pode ser desfeita. Confirme antes de clicar.

---

## 6. Referência Visual da Interface

```
┌─────────────────────────────────────────────────────────────┐
│  CATÁLOGO JOGOS              Início  |  + Novo jogo         │  ← Header
├─────────────────────────────────────────────────────────────┤
│  Sua biblioteca de jogos                                    │  ← Hero
│  Acompanhe o que você já jogou...                           │
├─────────────────────────────────────────────────────────────┤
│  Todos os jogos                             [+ Novo jogo]   │
│  ┌────────────────────────────────────────────────────┐     │
│  │ 🎮 │ The Legend of Zelda: TotK  │  9.8  │ 🎮 Jogado │ [Editar] [Excluir] │
│  └────────────────────────────────────────────────────┘     │
│  ┌────────────────────────────────────────────────────┐     │
│  │ 🎮 │ Elden Ring                 │  9.5  │ ⏳ N.Jog. │ [Editar] [Excluir] │
│  └────────────────────────────────────────────────────┘     │
└─────────────────────────────────────────────────────────────┘
```

---

## 7. Tarefas Disponíveis

O projeto inclui tarefas automatizadas via `taskipy`:

| Comando           | Descrição |
|-------------------|-----------|
| `uv run task run` | Inicia o servidor de desenvolvimento com hot-reload |
| `uv run task lint`| Verifica problemas de estilo com `ruff` |
| `uv run task format` | Formata o código automaticamente com `ruff` |

---

## 8. Solução de Problemas

| Problema | Possível Causa | Solução |
|----------|----------------|---------|
| Erro ao conectar ao banco | `DATABASE_URL` incorreta ou ausente | Verifique o arquivo `.env` |
| Lista de gêneros vazia no formulário | Tabela `generos` não foi populada | Execute o SQL de inserção de gêneros (seção 3.4) |
| Erro 422 ao salvar | Campo obrigatório não preenchido | Preencha todos os campos marcados como obrigatórios |
| Página não carrega o estilo | Servidor não encontra `/static` | Certifique-se de rodar o servidor a partir da raiz do projeto |
| `uv: command not found` | `uv` não está instalado | Instale conforme as instruções em https://docs.astral.sh/uv/ |
