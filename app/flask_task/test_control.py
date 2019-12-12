import pytest
from app.test.fixture import app, client

#from app import create_app


def test_show(app,client):
    with client:
        response = client.get(f'/task-tracker/test')
        assert response.status_code == 200
        assert b'test' in response.data
    




