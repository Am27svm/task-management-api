from pydantic import BaseModel


class TaskSchema(BaseModel):
    title: str
    description: str
    is_completed: bool = False


class TaskUpdateSchema(BaseModel):
    title: str | None = None
    description: str | None = None
    is_completed: bool | None = None

