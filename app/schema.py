from .model import Task, State
from marshmallow import Schema, fields

class StateSchema(Schema):
    id = fields.Integer()
    state = fields.String()

class TaskSchema(Schema):
    id = fields.Integer()
    name = fields.String()
    state = fields.Nested(StateSchema())

