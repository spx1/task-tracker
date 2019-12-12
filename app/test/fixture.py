import pytest
from app import create_app

@pytest.fixture()
def app():
    return create_app("test")

@pytest.fixture()
def client(app):
    return app.test_client()

if __name__ == "__main__":
    a = app()
    c = client(app)