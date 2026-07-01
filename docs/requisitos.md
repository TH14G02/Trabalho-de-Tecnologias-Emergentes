# Requisitos do Sistema — Catálogo de Jogos

## 1. Visão Geral

O sistema é uma aplicação web para gerenciamento de uma biblioteca pessoal de jogos. O usuário pode cadastrar jogos, atribuir notas, marcar os que já jogou e organizá-los por gênero. A aplicação foi desenvolvida como trabalho final da disciplina de Tecnologias Emergentes no Instituto Federal do Piauí — Campus Piripiri.

---

## 2. Requisitos Funcionais

| ID    | Descrição |
|-------|-----------|
| RF-01 | O sistema deve listar todos os jogos cadastrados na página inicial. |
| RF-02 | O sistema deve permitir o cadastro de um novo jogo com os campos: título, produtor, ano de lançamento, gênero, nota e status de jogado. |
| RF-03 | O sistema deve permitir a edição de qualquer campo de um jogo já cadastrado. |
| RF-04 | O sistema deve permitir a exclusão de um jogo cadastrado. |
| RF-05 | O sistema deve exibir o gênero do jogo como uma tag visual na listagem. |
| RF-06 | O sistema deve exibir o status do jogo ("Jogado" ou "Não jogado") de forma visualmente distinta. |
| RF-07 | O sistema deve exibir a nota do jogo em destaque em cada card da listagem. |
| RF-08 | O campo "gênero" deve ser selecionado a partir de uma lista pré-cadastrada no banco de dados. |
| RF-09 | A página inicial (`/`) deve redirecionar automaticamente para a listagem de jogos (`/jogos`). |

---

## 3. Requisitos Não Funcionais

| ID     | Categoria       | Descrição |
|--------|-----------------|-----------|
| RNF-01 | Desempenho      | O sistema deve responder às requisições em menos de 500 ms em condições normais de uso. |
| RNF-02 | Usabilidade     | A interface deve ser responsiva, adaptando-se a telas de celular e desktop. |
| RNF-03 | Segurança       | A URL de conexão com o banco de dados não deve ser exposta no código-fonte; deve ser carregada via variável de ambiente (`.env`). |
| RNF-04 | Manutenibilidade | O código deve seguir o padrão de formatação do `ruff` e ser organizado em módulos separados (`main.py`, `models.py`, `database.py`). |
| RNF-05 | Portabilidade   | O sistema deve funcionar em qualquer ambiente com Python 3.12+ e acesso ao banco PostgreSQL. |
| RNF-06 | Disponibilidade | O banco de dados utiliza o Supabase como provedor, garantindo alta disponibilidade gerenciada. |

---

## 4. Regras de Negócio

- **RN-01:** A nota de um jogo deve estar no intervalo de 0,0 a 10,0.
- **RN-02:** Os campos título, produtor, ano e gênero são obrigatórios para o cadastro de um jogo.
- **RN-03:** O campo "jogado" é opcional e possui valor padrão `False` (não jogado).
- **RN-04:** Um gênero só pode ser excluído se não houver jogos vinculados a ele (restrição de chave estrangeira no banco).
- **RN-05:** O ano de lançamento deve ser um número inteiro.

---

## 5. Escopo e Limitações

**Dentro do escopo:**
- CRUD completo de jogos.
- Categorização por gênero.
- Interface web com design temático.
- Persistência em banco de dados PostgreSQL na nuvem.

**Fora do escopo (versão atual):**
- Autenticação e controle de acesso por usuário.
- Upload de imagens de capa dos jogos.
- Sistema de busca e filtragem por gênero, nota ou status.
- API RESTful com retorno JSON para consumo externo.
- CRUD de gêneros pela interface web.
