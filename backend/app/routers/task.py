from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from starlette.status import HTTP_401_UNAUTHORIZED
from app.schemas.task import TaskCreate, TaskCreateResponse
from app.services.user_service import create_user
from app.database import get_db
from app.models.task import Task
from app.models.user import User

router = APIRouter()

"""
@router.post("/", response_model=TaskCreateResponse, status_code=status.HTTP_201_CREATED)
def create_task_endpoint(task: TaskCreate, db: Session = Depends(get_db)):
    # Check if user already exists
    user = db.query(User).filter(User.id == task.id_Usuario).first()
    if user is None:
        raise HTTPException(HTTP_401_UNAUTHORIZED, detail="You are not authorized to perform this action")
    return create_user(db, user)
"""
