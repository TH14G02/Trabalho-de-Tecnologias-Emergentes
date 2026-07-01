# Fluxo do Sistema — Catálogo de Jogos

## 1. Fluxo Geral de Navegação

```
                         ┌─────────────────┐
                         │   Acessa  "/"   │
                         └────────┬────────┘
                                  │ Redirect 302
                         ┌────────▼────────┐
                         │  GET /jogos     │
                         │  (lista.html)   │
                         └────────┬────────┘
                                  │
           ┌──────────────────────┼──────────────────────┐
           │                      │                      │
  ┌────────▼────────┐    ┌────────▼─────────┐  ┌────────▼────────┐
  │ Clica "+ Novo"  │    │  Clica "Editar"  │  │ Clica "Excluir" │
  └────────┬────────┘    └────────┬─────────┘  └────────┬────────┘
           │                      │                      │
  ┌────────▼────────┐    ┌────────▼─────────┐  ┌────────▼────────┐
  │ GET /jogos/novo │    │ GET /jogos/{id}/ │  │POST /jogos/{id}/│
  │  (form.html)    │    │     editar       │  │    excluir      │
  └────────┬────────┘    │  (form.html)     │  └────────┬────────┘
           │             └────────┬─────────┘           │
  ┌────────▼────────┐    ┌────────▼─────────┐           │
  │ Preenche e      │    │ Edita e submete  │           │
  │ submete form    │    │   o formulário   │           │
  └────────┬────────┘    └────────┬─────────┘           │
           │                      │                      │
  ┌────────▼────────┐    ┌────────▼─────────┐           │
  │  POST /jogos    │    │POST /jogos/{id}/ │           │
  │  (cria jogo)   │    │     editar       │           │
  └────────┬────────┘    └────────┬─────────┘           │
           │                      │                      │
           └──────────────────────┼──────────────────────┘
                                  │ Redirect 303
                         ┌────────▼────────┐
                         │  GET /jogos     │
                         │  (lista.html)   │
                         └─────────────────┘
```

---

## 2. Fluxo de Criação de um Jogo

```
Usuário                     FastAPI                    Banco de Dados
   │                            │                            │
   │── GET /jogos/novo ────────►│                            │
   │                            │── SELECT * FROM generos ──►│
   │                            │◄─ lista de gêneros ────────│
   │◄── form.html (vazio) ──────│                            │
   │                            │                            │
   │── POST /jogos (form data) ►│                            │
   │                            │── INSERT INTO jogos ───────►│
   │                            │◄── OK ─────────────────────│
   │◄── 303 Redirect /jogos ────│                            │
   │                            │                            │
   │── GET /jogos ─────────────►│                            │
   │                            │── SELECT * FROM jogos ─────►│
   │                            │◄─ lista de jogos ───────────│
   │◄── lista.html ─────────────│                            │
```

---

## 3. Fluxo de Edição de um Jogo

```
Usuário                     FastAPI                    Banco de Dados
   │                            │                            │
   │── GET /jogos/{id}/editar ─►│                            │
   │                            │── SELECT jogos WHERE id ──►│
   │                            │── SELECT * FROM generos ──►│
   │                            │◄─ dados do jogo + gêneros ─│
   │◄── form.html (preenchido) ─│                            │
   │                            │                            │
   │── POST /jogos/{id}/editar ►│                            │
   │   (form data com changes)  │                            │
   │                            │── UPDATE jogos SET ... ────►│
   │                            │◄── OK ─────────────────────│
   │◄── 303 Redirect /jogos ────│                            │
```

---

## 4. Fluxo de Exclusão de um Jogo

```
Usuário                     FastAPI                    Banco de Dados
   │                            │                            │
   │── POST /jogos/{id}/excluir►│                            │
   │   (via botão no form)      │                            │
   │                            │── DELETE FROM jogos ───────►│
   │                            │   WHERE id = {id}          │
   │                            │◄── OK ─────────────────────│
   │◄── 303 Redirect /jogos ────│                            │
```

---

## 5. Fluxo de Inicialização da Aplicação

```
1. Aplicação FastAPI inicia (uvicorn)
         │
2. Context manager "lifespan" executa
         │
3. Base.metadata.create_all(bind=engine)
         │
   ┌─────▼──────────────────────────────────┐
   │ Verifica e cria tabelas se não existem │
   │  - generos                             │
   │  - jogos                               │
   └─────────────────────────────────────────┘
         │
4. Aplicação disponível para receber requisições
         │
5. Rota estática /static montada (CSS)
         │
6. Sistema pronto em http://localhost:8000
```

---

## 6. Estados de um Jogo

```
         ┌──────────────┐
         │   Cadastrado │
         │ jogado=False │◄──── Criação via /jogos (POST)
         └──────┬───────┘
                │
         Edição via /jogos/{id}/editar
                │
         ┌──────▼───────┐
         │   Atualizado │
         │ jogado=True  │
         └──────┬───────┘
                │
         Exclusão via /jogos/{id}/excluir
                │
         ┌──────▼───────┐
         │   Removido   │
         │  (deletado)  │
         └──────────────┘
```
