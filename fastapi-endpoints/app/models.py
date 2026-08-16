from pydantic import BaseModel


class Todo(BaseModel):
    todo_id: int
