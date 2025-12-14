from pydantic import BaseModel
from typing import Literal

class TaskCreate(BaseModel):
    title: str
    priority: Literal["low", "medium", "high"]