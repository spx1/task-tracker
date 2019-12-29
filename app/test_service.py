from flask_sqlalchemy import SQLAlchemy
from app.test.fixture import app, db
from .model import Task
from .service import TaskService

def test_get_all(db: SQLAlchemy):
    t1 : Task = Task(id=1, name='Task Number 1')
    t2 : Task = Task(id=2, name='Task Number 2')
    db.session.add(t1)
    db.session.add(t2)
    db.session.commit()

    res = TaskService.get_all()

    assert len(res)==2
    assert t1 in res and t2 in res