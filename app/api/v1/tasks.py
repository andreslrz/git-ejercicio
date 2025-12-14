from fastapi import APIRouter
from app.services.task_service import TaskService
from app.repositories.task_repository import TaskRepository

router = APIRouter(prefix="/tasks", tags=["tasks"])
service = TaskService(TaskRepository())

@router.post("/")
def create_task(title: str):
    return service.create_task(title)

@router.get("/")
def list_tasks():
    return service.list_tasks()
