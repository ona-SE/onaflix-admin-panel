import pytest
from app import create_app


@pytest.fixture
def client():
    app = create_app({
        'TESTING': True,
        'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:',
    })
    with app.test_client() as client:
        yield client


def test_health(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json['status'] == 'ok'


def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert 'OnaFlix Admin Panel' in response.json['service']


def test_login(client):
    response = client.post('/auth/login', json={
        'email': 'admin@onaflix.com',
        'password': 'password',
    })
    assert response.status_code == 200
    assert 'token' in response.json


def test_login_missing_fields(client):
    response = client.post('/auth/login', json={})
    assert response.status_code == 400
