
def test_get_users(client):
    response = client.get('/users')
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)

def test_get_user(client):
    client.post('/users', json={"name": "Wojciech", "lastname": "Oczkowski"})
    response = client.get('/users/1')
    assert response.status_code == 200
    assert response.get_json() == {"id": 1, "name": "Wojciech", "lastname": "Oczkowski"}

def test_create_user(client):
    response = client.post('/users', json={"name": "Wojciech", "lastname": "Oczkowski"})
    assert response.status_code == 201

def test_patch_user(client):
    client.post('/users', json={"name": "Wojciech", "lastname": "Oczkowski"})
    response = client.patch('/users/1', json={"name": "Jan"})
    assert response.status_code == 204
    response = client.get('/users/1')
    assert response.get_json() == {"id": 1, "name": "Jan", "lastname": "Oczkowski"}

def test_put_user(client):
    client.post('/users', json={"name": "Wojciech", "lastname": "Oczkowski"})
    response = client.put('/users/1', json={"name": "Jan", "lastname": "Kowalski"})
    assert response.status_code == 204
    response = client.get('/users/1')
    assert response.get_json() == {"id": 1, "name": "Jan", "lastname": "Kowalski"}

def test_delete_user(client):
    client.post('/users', json={"name": "Wojciech", "lastname": "Oczkowski"})
    response = client.delete('/users/1')
    assert response.status_code == 204
    response = client.get('/users/1')
    assert response.status_code == 404

def test_patch_user_invalid_id(client):
    response = client.patch('/users/999', json={"name": "Jan"})
    assert response.status_code == 400

def test_patch_user_invalid_body(client):
    client.post('/users', json={"name": "Wojciech", "lastname": "Oczkowski"})
    response = client.patch('/users/1', json={"age": 30})
    assert response.status_code == 400

def test_put_user_invalid_body(client):
    response = client.put('/users/1', json={"age": 30})
    assert response.status_code == 400

def test_delete_user_invalid_id(client):
    response = client.delete('/users/999')
    assert response.status_code == 400
