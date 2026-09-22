class Todo:
    """Representa uma tarefa da lista."""

    def __init__(self, todo_id: int, title: str, completed: bool = False):
        self.id = todo_id
        self.title = title
        self.completed = completed

    def toggle(self):
        """Alterna o estado da tarefa entre concluída e não concluída."""
        self.completed = not self.completed

    def to_dict(self):
        """Converte o objeto para um dicionário que pode virar JSON."""
        return {
            "id": self.id,
            "title": self.title,
            "completed": self.completed,
        }
