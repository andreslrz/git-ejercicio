from app.repositories.task_repository import TaskRepository

class TaskService:
    def __init__(self, repository: TaskRepository):
        self.repository = repository

    def create_task(self, title: str):
        return self.repository.save(title)

    def list_tasks(self):
        return self.repository.list()
    
    def complete_task(self, task_id):
        task = self.repository._tasks[task_id]
        task.completed = True
        return task
