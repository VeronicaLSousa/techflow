from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulação de banco de dados em memória
tasks = []
current_id = 1

@app.route("/")
def home():
    return "TechFlow Task Manager - API ativa"

# READ - listar tarefas
@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)

# CREATE - criar tarefa
@app.route("/tasks", methods=["POST"])
def create_task():
    global current_id

    data = request.get_json()

    if not data or "title" not in data:
        return jsonify({"error": "Título é obrigatório"}), 400

    task = {
        "id": current_id,
        "title": data["title"],
        "completed": False
    }

    tasks.append(task)
    current_id += 1
    return jsonify(task), 201

# UPDATE - atualizar tarefa
@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            return jsonify(task)
    return jsonify({"error": "Tarefa não encontrada"}), 404

# DELETE - excluir tarefa
@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task["id"] != task_id]
    return "", 204

if __name__ == "__main__":
    app.run(debug=True)
