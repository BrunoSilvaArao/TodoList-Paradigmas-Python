from models.todo import Todo


class TodoService:
    """Gerencia as regras e operações da lista de tarefas."""

    def __init__(self):
        self._todos = [
            Todo(1, "Conhecer o contrato da API", True),
            Todo(2, "Implementar o primeiro paradigma", False),
        ]

    def list_all(self):
        return self._todos

    def create(self, title: str):
        if not isinstance(title, str) or not title.strip():
            raise ValueError("O título da tarefa é obrigatório.")

        next_id = 1
        for todo in self._todos:
            if todo.id >= next_id:
                next_id = todo.id + 1

        new_todo = Todo(next_id, title.strip(), False)
        self._todos.append(new_todo)
        return new_todo

    def find_by_id(self, todo_id: int):
        for todo in self._todos:
            if todo.id == todo_id:
                return todo
        return None

    def toggle(self, todo_id: int):
        todo = self.find_by_id(todo_id)
        if todo is None:
            return None

        todo.toggle()
        return todo

    def delete(self, todo_id: int):
        todo = self.find_by_id(todo_id)
        if todo is None:
            return False

        self._todos.remove(todo)
        return True
