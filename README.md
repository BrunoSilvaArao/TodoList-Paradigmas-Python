# Todo List API em Python Orientada a Objetos

Projeto acadêmico desenvolvido em **Python** utilizando o paradigma de **Orientação a Objetos (POO)**.

A aplicação consiste em uma API REST simples para gerenciamento de tarefas, permitindo listar, criar, alterar o status e excluir tarefas.

## Tecnologias utilizadas

- Python
- Flask
- Programação Orientada a Objetos
- API REST
- JSON

## Funcionalidades

| Método | Rota | Função |
|---|---|---|
| GET | `/todos` | Lista todas as tarefas |
| POST | `/todos` | Cria uma nova tarefa |
| PATCH | `/todos/{id}/toggle` | Altera o status da tarefa |
| DELETE | `/todos/{id}` | Exclui uma tarefa |

## Estrutura do projeto

```text
Objetos orientados a Python/
├── app.py
├── models/
│   └── todo.py
├── services/
│   └── todo_service.py
├── requirements.txt
└── TodoListApi.http
```

## Orientação a Objetos

O projeto foi organizado em classes para separar responsabilidades:

- **Todo**: representa uma tarefa.
- **TodoService**: contém as regras de negócio e controla a lista de tarefas.
- **TodoAPI**: configura as rotas da API com Flask.

Com isso, o projeto utiliza conceitos como **classes, objetos, métodos, encapsulamento e separação de responsabilidades**.

## Como executar

### 1. Clonar o repositório

```bash
git clone https://github.com/BrunoSilvaArao/TodoList-Paradigmas-Python.git
```

### 2. Entrar na pasta do projeto

```bash
cd TodoList-Paradigmas-Python
cd "Objetos orientados a Python"
```

### 3. Instalar as dependências

No Windows:

```bash
py -m pip install -r requirements.txt
```

Ou:

```bash
python -m pip install -r requirements.txt
```

### 4. Executar a API

```bash
py app.py
```

Ou:

```bash
python app.py
```

A API ficará disponível em:

```text
http://127.0.0.1:5000
```

## Exemplos de uso

### Listar tarefas

```http
GET http://127.0.0.1:5000/todos
```

### Criar uma tarefa

```http
POST http://127.0.0.1:5000/todos
Content-Type: application/json

{
  "title": "Estudar orientação a objetos em Python"
}
```

### Alterar o status da tarefa

```http
PATCH http://127.0.0.1:5000/todos/1/toggle
```

### Excluir uma tarefa

```http
DELETE http://127.0.0.1:5000/todos/1
```

## Códigos de resposta

- `200 OK` — operação realizada com sucesso.
- `201 Created` — tarefa criada com sucesso.
- `204 No Content` — tarefa excluída com sucesso.
- `400 Bad Request` — dados inválidos.
- `404 Not Found` — tarefa não encontrada.

## Testes

As requisições podem ser testadas pelo arquivo:

```text
TodoListApi.http
```

No Visual Studio Code, pode ser utilizada a extensão **REST Client** para executar as requisições diretamente pelo arquivo.

Fluxo sugerido:

```text
GET → POST → GET → PATCH → GET → DELETE → GET
```

## Observação

Os dados são armazenados em memória. Portanto, ao encerrar e iniciar novamente a aplicação, as alterações feitas durante os testes não permanecem salvas.

## Autor

**Bruno Silva Arão**

Curso de Ciência da Computação
