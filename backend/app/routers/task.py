from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.models.category import Category
from app.models.task import Task
from app.schemas.task import TaskCreate, TaskSchema, TaskUpdate
from app.database import get_db
from app.dependencies import get_current_user
from app.models.user import User
from app.services.task_service import create_task, delete_task, update_task

router = APIRouter()


@router.get("/{id}", response_model=TaskSchema, status_code=status.HTTP_200_OK)
def get_task_endpoint(id: int, user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    task = db.query(Task).filter_by(id=id).first()
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_BAD_REQUEST,
            detail="Task does not exist",
        )
    if task.id_Usuario != user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You are not authorized to perform this action"
        )
    return task

@router.post("/", response_model=TaskSchema, status_code=status.HTTP_201_CREATED)
def create_task_endpoint(task_create: TaskCreate, user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    # Check if user already exists
    if task_create.id_Usuario != user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You are not authorized to perform this action"
        )
    if not db.query(Category).filter_by(id=task_create.id_Categoria).first():
        raise HTTPException(
            status_code=status.HTTP_404_BAD_REQUEST,
            detail="Category does not exist",
        )
    return create_task(db, task_create)

@router.put("/{id}", response_model=TaskSchema, status_code=status.HTTP_202_ACCEPTED)
def update_task_endpoint(id: int, task_update: TaskUpdate, user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    task = db.query(Task).filter_by(id=id).first()
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_BAD_REQUEST,
            detail="Task does not exist",
        )
    if task.id_Usuario != user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You are not authorized to perform this action"
        )
    if not (task_update.estado or task_update.texto_tarea):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Empty request"
        )
    return update_task(db, task, task_update)

@router.delete("/{id}", response_model=None, status_code=status.HTTP_204_NO_CONTENT)
def delete_task_endpoint(id: int, user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    task = db.query(Task).filter_by(id=id).first()
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_BAD_REQUEST,
            detail="Task does not exist",
        )
    if task.id_Usuario != user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You are not authorized to perform this action"
        )
    delete_task(db, task)
