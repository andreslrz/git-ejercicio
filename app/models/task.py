from dataclasses import dataclass
from uuid import UUID, uuid4

@dataclass
class Task:
    id: UUID
    title: str
    completed: bool = False
