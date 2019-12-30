from app import db
from .interface import StateInterface,TaskInterface

class State(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(55),unique=True,nullable=False)

    def update(self, state_changes : StateInterface):
        for key,value in state_changes.items():
            setattr(self, key, value)
        return self

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(55),unique=True,nullable=False)
    state_id = db.Column(db.Integer, db.ForeignKey('state.id'))
    state = db.relationship('State',backref=db.backref('tasks',lazy=True))

    def update(self, task_changes : TaskInterface):
        for key,value in task_changes.items():
            setattr(self, key, value)
        return self
