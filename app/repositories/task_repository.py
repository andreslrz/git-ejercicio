from app.models.task import Task
from uuid import uuid4

class TaskRepository:
    def __init__(self):
        self._tasks = {}

    def save(self, title: str) -> Task:
        task = Task(id=uuid4(), title=title)
        self._tasks[task.id] = task
        return task

    def list(self):
        return list(self._tasks.values())
