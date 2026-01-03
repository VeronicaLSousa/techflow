import json
from src.app import app


def test_get_tasks_empty():
    """
    Testa se a listagem inicial de tarefas retorna uma lista vazia
    """
    client = app.test_client()
    response = client.get("/tasks")

    assert response.status_code == 200
    assert response.json == []


def test_create_task_success():
    """
    Testa a criação de uma tarefa válida
    """
    client = app.test_client()

    response = client.post(
        "/tasks",
        data=json.dumps({"title": "Teste de tarefa"}),
        content_type="application/json"
    )

    assert response.status_code == 201
    assert response.json["title"] == "Teste de tarefa"
    assert response.json["completed"] is False


def test_create_task_without_title():
    """
    Testa validação: não permitir criar tarefa sem título
    """
    client = app.test_client()

    response = client.post(
        "/tasks",
        data=json.dumps({}),
        content_type="application/json"
    )

    assert response.status_code == 400
    assert "Título é obrigatório" in response.get_data(as_text=True)

def test_create_task_without_title():
    """
    Testa validação: não permitir criar tarefa sem título
    """
    client = app.test_client()

    response = client.post(
        "/tasks",
        json={},  # forma correta
    )

    assert response.status_code == 400
    assert response.json["error"] == "Título é obrigatório"
