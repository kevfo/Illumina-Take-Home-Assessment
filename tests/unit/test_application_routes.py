import sys, os, pytest

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, project_root)
from app import app

@pytest.fixture()
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# == BEGIN ACTUAL TESTING ==

def test_webpage_should_be_accessible(client):
    response = client.get('/')
    assert response.status_code == 200

def test_controllers_should_work_with_valid_data(client):
    r1, r2 = client.post('/to_roman/23'), client.post('/to_arabic/IV')
    assert r1.status_code == 200
    assert r2.status_code == 200

def test_controllers_should_work_fail_with_invalid_data(client):
    try:
        r1 = client.post('/to_roman/ou').json()
    except:
        assert TypeError
    
    try:
        r2 = client.post('/to_arabic/4V').json()
    except:
        assert TypeError
