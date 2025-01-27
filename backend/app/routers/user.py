from datetime import datetime
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from jose import exceptions, jwt
from pydantic import ValidationError
from sqlalchemy.orm import Session
from app.schemas.user import AccessTokenSchema, RefreshTokenSchema, TokenPayload, TokenSchema, UserCreate, UserSchema, UserTasksResponse
from app.services.user_service import create_user
from app.database import get_db
from app.models.user import User
from app.models.task import Task
from app.schemas.task import TaskSchema
from app.utils import (
    ALGORITHM,
    JWT_REFRESH_SECRET_KEY,
    create_access_token,
    create_refresh_token,
    verify_password
)
from app.dependencies import get_current_user

router = APIRouter()

@router.post("/", response_model=UserSchema, status_code=status.HTTP_201_CREATED)
def create_user_endpoint(user: UserCreate, db: Session = Depends(get_db)):
    if db.query(User).filter_by(nombre_usuario=user.nombre_usuario).first():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User already registered",
        )
    return create_user(db, user)

@router.get('/me', summary='Get details of currently logged in user', response_model=UserSchema)
async def get_me(user: User = Depends(get_current_user)):
    return user

@router.post("/iniciar-sesion", response_model=TokenSchema, status_code=status.HTTP_201_CREATED)
def login_endpoint(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter_by(nombre_usuario=form_data.username).first()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password"
        )
    hashed_pass = user.contrasenia
    if not verify_password(form_data.password, hashed_pass):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password"
        )

    return {
        "access_token": create_access_token(user.id),
        "refresh_token": create_refresh_token(user.id),
    }

@router.post("/refrescar-token", response_model=AccessTokenSchema, status_code=status.HTTP_201_CREATED)
def refresh_endpoint(refresh_token: RefreshTokenSchema = Depends()):
    try:
        payload = jwt.decode(
            refresh_token.refresh_token, JWT_REFRESH_SECRET_KEY, algorithms=[ALGORITHM]
        )
        token_data = TokenPayload(**payload)

        if datetime.timestamp(token_data.exp) < datetime.timestamp(datetime.now()):
            raise HTTPException(
                status_code = status.HTTP_401_UNAUTHORIZED,
                detail="Token expired",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except(exceptions.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return {
        "access_token": create_access_token(token_data.sub),
    }

@router.get("/{id}/tareas", response_model=List[TaskSchema], status_code=status.HTTP_200_OK)
def get_user_tasks_endpoint(id: str, db: Session = Depends(get_db)):
    user = db.query(User).filter_by(id=id).first()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User does not exist"
        )
    tasks = db.query(Task).filter_by(id_Usuario=user.id).all()
    return tasks
