# Todo List — Paradigmas de Linguagens de Programação

Projeto desenvolvido para a disciplina de **Paradigmas de Linguagens de Programação**.

O objetivo do projeto é implementar uma API para uma aplicação de lista de tarefas (Todo List), utilizando diferentes linguagens e paradigmas de programação, permitindo comparar como cada paradigma organiza os dados, as regras e as alterações de estado da aplicação.

## Paradigmas e Linguagens

| Paradigma | Linguagem | Status |
|---|---|---|
| Imperativo | C# | ✅ Em desenvolvimento |
| Funcional | F# | ⏳ Pendente |
| Orientado a Objetos | Python | ✅ Implementado |

## Estrutura do Projeto

```text
TodoList-Paradigmas/
│
├── CSharp-Imperativo/
├── FSharp-Funcional/
├── Python-OrientadoObjetos/
└── README.md
```

A implementação em Python mantém o mesmo contrato básico da versão em C#: `GET /todos`, `POST /todos`, `PATCH /todos/{id}/toggle` e `DELETE /todos/{id}`.
