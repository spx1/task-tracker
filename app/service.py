from app import db
from typing import List
from .model import Task, State
from .interface import StateInterface, TaskInterface

class StateService:
    @staticmethod
    def get_all() -> List[State]:
        return State.query.all()

    @staticmethod
    def get_by_id(state_id : int) -> State:
        return State.query.filter_by(id=state_id).first()
    
    @staticmethod
    def create(new_attrs : StateInterface) -> State:
        state : State = State(name=new_attrs['name'])
        db.session.add(state)
        db.session.commit()
        return state

    @staticmethod
    def update(state_id : int, state_change_update : StateInterface) -> State:
        state : State = State.query.filter_by(id=state_id).first()
        state.update(state_change_update)
        db.session.commit()
        return state

    @staticmethod
    def delete_by_id(state_id : int) -> List[int]:
        state : State = State.query.filter_by(id=state_id).first()
        if not state:
            return []
        db.session.delete(state)
        db.session.commit()
        return [state_id]
        
class TaskService:
    @staticmethod
    def get_all() -> List[Task]:
        return Task.query.all()

    @staticmethod
    def get_by_id(id : int) -> Task:
        return Task.query.filter_by(id=id).first()

    @staticmethod
    def create(new_attrs : TaskInterface) -> Task:
        task : Task = Task(name=new_attrs['name'],state_id=new_attrs['state_id'])
        db.session.add(task)
        db.session.commit()

        return task 

    @staticmethod
    def delete_by_id(id : int) -> List[int]:
        task : Task = Task.query.filter_by(id=id).first()
        if not task:
            return []
        db.session.delete(task)
        db.session.commit()
        return [id]
    
    @staticmethod
    def update_by_id(task_id : int, task_change_update : TaskInterface) -> Task:
        task : Task = Task.query.filter_by(id=task_id).first()
        task.update(task_change_update)
        db.session.commit()
        return task