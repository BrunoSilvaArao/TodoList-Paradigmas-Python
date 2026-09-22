from flask import Flask, jsonify, request
from flask_cors import CORS

from services.todo_service import TodoService


class TodoAPI:
    """Classe responsável pela configuração das rotas HTTP da API."""

    def __init__(self):
        self.app = Flask(__name__)
        self.service = TodoService()

        CORS(
            self.app,
            resources={r"/*": {"origins": "https://vmussak.github.io"}},
        )

        self._configure_routes()

    def _configure_routes(self):
        @self.app.get("/todos")
        def list_todos():
            todos = self.service.list_all()
            return jsonify([todo.to_dict() for todo in todos]), 200

        @self.app.post("/todos")
        def create_todo():
            data = request.get_json(silent=True) or {}

            try:
                todo = self.service.create(data.get("title"))
            except ValueError as error:
                return jsonify({"error": str(error)}), 400

            response = jsonify(todo.to_dict())
            response.status_code = 201
            response.headers["Location"] = f"/todos/{todo.id}"
            return response

        @self.app.patch("/todos/<int:todo_id>/toggle")
        def toggle_todo(todo_id):
            todo = self.service.toggle(todo_id)

            if todo is None:
                return jsonify({"error": "Tarefa não encontrada."}), 404

            return jsonify(todo.to_dict()), 200

        @self.app.delete("/todos/<int:todo_id>")
        def delete_todo(todo_id):
            deleted = self.service.delete(todo_id)

            if not deleted:
                return jsonify({"error": "Tarefa não encontrada."}), 404

            return "", 204

    def run(self):
        self.app.run(host="0.0.0.0", port=5000, debug=True)


if __name__ == "__main__":
    api = TodoAPI()
    api.run()
