from fastapi import APIRouter

router = APIRouter()

tasks = [
    {"id": 1, "title": "Comprar leche"},
    {"id": 2, "title": "Pagar servicios"},
]

@router.get("/tasks")
def get_tasks():
    return tasks