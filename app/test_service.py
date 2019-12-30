from flask_sqlalchemy import SQLAlchemy
from app.test.fixture import app, db
from .model import Task, State
from .service import TaskService, StateService
from .interface import TaskInterface, StateInterface
from typing import List

def test_task_get_all(db: SQLAlchemy):
    t1 : Task = Task(id=1, name='Task Number 1')
    t2 : Task = Task(id=2, name='Task Number 2')
    db.session.add(t1)
    db.session.add(t2)
    db.session.commit()

    res = TaskService.get_all()

    assert len(res)==2
    assert t1 in res and t2 in res

def test_task_create(db: SQLAlchemy):
    new_args : TaskInterface = TaskInterface(name='Task1',state_id=1)
    TaskService.create(new_args)

    result : List[Task] = Task.query.all()
    assert len(result)==1

    for key,value in new_args.items():
        assert getattr(result[0],key)==value

def test_task_update(db: SQLAlchemy):
    state1 : State = State(id=1,name="State1")
    state2 : State = State(id=2,name="State2")
    task : Task = Task(id=1,name='Task1',state_id=1)
    db.session.add(state1)
    db.session.add(state2)
    db.session.add(task)
    db.session.commit()

    task_changes : TaskInterface = TaskInterface(name='UpdateName1',state_id=2)
    TaskService.update_by_id(1, task_changes)

    results : List[Task] = Task.query.all()
    assert len(results)==1

    for key,value in task_changes.items():
        assert getattr(results[0],key)==value

def test_state_get_all(db: SQLAlchemy):
    t1 : State = State(id=1, name='Open')
    t2 : State = State(id=2, name='Closed')
    db.session.add(t1)
    db.session.add(t2)
    db.session.commit()

    states = StateService.get_all()

    assert len(states)==2
    assert t1 in states and t2 in states

def test_state_create(db: SQLAlchemy):
    si : StateInterface = StateInterface(name='Test')
    StateService.create(si)

    results : List[State] = State.query.all()
    assert len(results)==1

    for k in si.keys():
        assert getattr(results[0],k) == si[k]
    
def test_state_update(db: SQLAlchemy):
    st : State = State(id=1,name='Test')
    db.session.add(st)
    db.session.commit()

    si : StateInterface = StateInterface(name='Updated Name')
    StateService.update(st.id, si)
    
    results : List[State] = State.query.all()
    assert len(results)==1

    for k in si.keys():
        assert getattr(results[0],k) == si[k]

