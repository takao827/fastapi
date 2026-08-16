from fastapi import FastAPI

from app.models import Todo

app = FastAPI()


@app.get("/todos")
def get_todos() -> list[Todo]:
    return [Todo(todo_id=1)]


@app.post("/todos")
def post_todos() -> Todo:
    return Todo(todo_id=2)
