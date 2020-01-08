from unittest.mock import patch
import pytest
from app.test.fixture import app, client
from app.model import Task, State
from app.schema import TaskSchema
from app.service import TaskService
from app.interface import TaskInterface
from app.flask_task import BASE_ROUTE

#from app import create_app
def make_task(id=123,name="Test Task",state="Test State") -> Task:
    state = State(id=1, name="Test State")
    return Task(id=id, name=name, state=state) 


def test_show(app,client):
    with client:
        response = client.get(f'/{BASE_ROUTE}/test')
        assert response.status_code == 200
        assert b'test' in response.data

class TestControlResource:
    @patch.object(
        TaskService,
        "get_all",
        lambda : [
            make_task( 1, "Test Task 1", "Open"),
            make_task( 2, "Test Task 2", "In Progress")
        ]
    )
    def test_get_all(self,client):
        with client:
            response = client.get(f"/{BASE_ROUTE}/app/get_all",follow_redirects=True)
            assert response.status_code == 200
            expected = TaskSchema(many=True).dump(
                [
                    make_task(1, "Test Task 1", "Open"),
                    make_task(2, "Test Task 2", "In Progress")
                ]
            )

            for r in response.get_json():
                assert r in expected



