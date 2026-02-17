def test_create_task(client):

    response = client.post("/api/v1/tasks/", json={"title": "Test Task", "description": "Testing"})

    assert response.status_code == 200
    data = response.json()

    assert data["title"] == "Test Task"
    assert data["status"] == "pending"


def test_list_tasks(client):

    client.post("/api/v1/tasks/", json={"title": "Another Task"})

    response = client.get("/api/v1/tasks/")
    assert response.status_code == 200
    assert len(response.json()) == 1
