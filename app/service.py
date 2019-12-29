from app import db
from typing import List
from .model import Task

class TaskService:
    @staticmethod
    def get_all() -> List[Task]:
        return Task.query.all()

    
