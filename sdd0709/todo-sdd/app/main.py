import os
from typing import Optional

from fastapi import Depends, FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.crud import create_todo, delete_todo, get_todo, get_todos, update_todo
from app.database import get_db, init_db
from app.schemas import TodoCreate, TodoRead, TodoUpdate

os.makedirs("app/templates", exist_ok=True)

app = FastAPI()

templates = Jinja2Templates(directory="app/templates")

init_db()


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse(request, "index.html", {"request": request})


@app.get("/api/todos", response_model=list[TodoRead])
def list_todos(status: Optional[str] = "all", db: Session = Depends(get_db)):
    if status not in {"all", "active", "completed"}:
        raise HTTPException(status_code=400, detail="invalid status")
    todos = get_todos(db, status=status if status != "all" else None)
    return todos


@app.post("/api/todos", response_model=TodoRead)
def create_todo_api(todo: TodoCreate, db: Session = Depends(get_db)):
    return create_todo(db, todo)


@app.patch("/api/todos/{todo_id}", response_model=TodoRead)
def update_todo_api(todo_id: int, todo_update: TodoUpdate, db: Session = Depends(get_db)):
    todo = get_todo(db, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="todo not found")
    return update_todo(db, todo, todo_update)


@app.delete("/api/todos/{todo_id}")
def delete_todo_api(todo_id: int, db: Session = Depends(get_db)):
    todo = get_todo(db, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="todo not found")
    delete_todo(db, todo)
    return {"message": "deleted"}


@app.get("/api/todos/{todo_id}", response_model=TodoRead)
def get_todo_api(todo_id: int, db: Session = Depends(get_db)):
    todo = get_todo(db, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="todo not found")
    return todo
