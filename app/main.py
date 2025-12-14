from fastapi import FastAPI
from app.api.v1.tasks import router as task_router_v1

app = FastAPI(title="Task Manager API")

app.include_router(task_router_v1, prefix="/api/v1")