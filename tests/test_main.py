import pytest
from fastapi.testclient import TestClient
from app.main import app
@pytest.fixture
def auth_token(client,test_task,another_users_task):
    login_response = client.post(
        "/login",
        json={
            "username" : "ali",
            "password" : "ali"
        }
    )
    print("Status:", login_response.status_code)
    print("Response", login_response.json())
    assert login_response.status_code == 200 , login_response.json()
    return login_response.json()["token"]
def test_delete_another_user_task(client,auth_token,another_users_task):
    response = client.delete(
        f"/tasks/{another_users_task.id}",
        headers = {"Authorization" : f"Bearer {auth_token}"}
    )
    print(response.status_code, response.json())
    assert response.status_code == 404
def test_show_task(client,auth_token):
    response = client.get(
        "/tasks",
        headers = {"Authorization" : f"Bearer {auth_token}"}
    )
    print(response.status_code, response.json())
    assert response.status_code == 200


def test_tasks_without_token(client):
    response = client.get(
        "/tasks"
    )
    print(response.status_code, response.json())
    assert response.status_code == 401
def test_tasks_not_exists(client,auth_token,test_task):
    response = client.get(
        f"/tasks/22",
        headers = {"Authorization" : f"Bearer {auth_token}"}
    )
    print()
    assert response.status_code==404
def test_create_task(auth_token,client,test_project):
    response = client.post(
        "/tasks",
        json={
            "title": "Python Task",
            "status": "todo",
            "priority": "high",
            "project_id": test_project.id
        },
        headers = {"Authorization" : f"Bearer {auth_token}"}   
    )
    print(response.status_code, response.json())
    assert response.status_code == 201
# def test_all_users(auth_token,client):
#     response = client.get(
#         "/users",
#         headers = {"Authorization" : f"Bearer {auth_token}"}
#     )
#     print(response.status_code,response.json())
#     assert response.status_code == 401
def test_for_seeing_all_task(client,auth_token):
    response = client.get(
        "/tasks",
        headers = {"Authorization" : f"Bearer {auth_token}"}
    )
    print(response.status_code,response.json())
    assert response.status_code == 200
def test_for_seeing_task(client,auth_token,test_task):
    response = client.get(
        f"/tasks/{test_task.id}",
        headers = {"Authorization" : f"Bearer {auth_token}"}
    )
    print(response.status_code,response.json())
    assert response.status_code == 200
def test_for_other_user_task(client,auth_token,another_users_task):
    response = client.get(
        f"/tasks/{another_users_task.id}",
        headers = {"Authorization" : f"Bearer {auth_token}"}
    )
    print(response.status_code,response.json())
    assert response.status_code == 404
def test_tasks_without_token(client):
    response = client.get(
        "/tasks",
        headers = {"Authorization" : "fake-token"}
    )
    print(response.status_code,response.json())
    assert response.status_code == 401
def test_create_task_invalid_status(client,test_project,auth_token):
    response = client.post(
        "/tasks",
        json={
            "title": "Python Task",
            "status": "started",
            "priority": "high",
            "project_id": test_project.id
        },
        headers = {"Authorization" : f"Bearer {auth_token}"}

    )
    print(response.status_code, response.json())
    assert response.status_code == 422

def test_update_task_invalid_status(client,auth_token,test_task):
    response = client.patch(
        f"/tasks/{test_task.id}",
        json={"status" : "started"},
        headers = {"Authorization" : f"Bearer {auth_token}"}
    )
    print(response.status_code,response.json())
    assert response.status_code == 422
