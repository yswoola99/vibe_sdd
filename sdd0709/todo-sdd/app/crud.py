from typing import Optional
from sqlalchemy.orm import Session

from app.models import Todo
from app.schemas import TodoCreate, TodoUpdate


def get_todos(db: Session, status: Optional[str] = None):
    query = db.query(Todo)
    if status == "active":
        query = query.filter(Todo.completed.is_(False))
    elif status == "completed":
        query = query.filter(Todo.completed.is_(True))
    return query.order_by(Todo.id.asc()).all()


def create_todo(db: Session, todo_in: TodoCreate) -> Todo:
    todo = Todo(title=todo_in.title, completed=False)
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo


def get_todo(db: Session, todo_id: int) -> Optional[Todo]:
    return db.query(Todo).filter(Todo.id == todo_id).first()


def update_todo(db: Session, todo: Todo, todo_in: TodoUpdate) -> Todo:
    if todo_in.completed is not None:
        todo.completed = todo_in.completed
    db.commit()
    db.refresh(todo)
    return todo


def delete_todo(db: Session, todo: Todo) -> None:
    db.delete(todo)
    db.commit()
