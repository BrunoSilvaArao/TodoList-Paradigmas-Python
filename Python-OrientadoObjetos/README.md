# API Todo List — Python Orientado a Objetos

Versão em **Python** da API Todo List desenvolvida para a disciplina de **Paradigmas de Linguagens de Programação**.

Nesta implementação, o paradigma utilizado é **Orientação a Objetos (POO)**.

## Estrutura

```text
Python-OrientadoObjetos/
├── app.py
├── models/
│   └── todo.py
├── services/
│   └── todo_service.py
├── requirements.txt
└── TodoListApi.http
```

## Onde aparece a Orientação a Objetos?

- `Todo`: classe que representa uma tarefa.
- `TodoService`: classe que guarda as tarefas e contém as regras da aplicação.
- `TodoAPI`: classe que configura a API e suas rotas.
- Cada tarefa criada é um **objeto** da classe `Todo`.
- Os comportamentos são organizados em **métodos**, como `toggle()`, `create()` e `delete()`.
- A lista `_todos` fica dentro do serviço, ajudando a demonstrar **encapsulamento**.

## Rotas

| Método | Rota | Função |
|---|---|---|
| GET | `/todos` | Lista todas as tarefas |
| POST | `/todos` | Cria uma nova tarefa |
| PATCH | `/todos/{id}/toggle` | Alterna o status da tarefa |
| DELETE | `/todos/{id}` | Exclui uma tarefa |

## Como executar

Abra o terminal dentro da pasta `Python-OrientadoObjetos`.

### 1. Criar ambiente virtual (opcional, mas recomendado)

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### 2. Instalar dependências

```bash
pip install -r requirements.txt
```

### 3. Iniciar a API

```bash
python app.py
```

A API ficará disponível em:

```text
http://127.0.0.1:5000
```

## Exemplo para criar tarefa

Requisição:

```http
POST /todos
Content-Type: application/json
```

Corpo JSON:

```json
{
  "title": "Estudar Python"
}
```

Resposta esperada:

```json
{
  "id": 3,
  "title": "Estudar Python",
  "completed": false
}
```

> Observação: os dados ficam apenas na memória. Ao encerrar e iniciar novamente o programa, a lista volta ao estado inicial. Isso segue a proposta da API de exemplo em C#.
