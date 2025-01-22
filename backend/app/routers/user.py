from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.schemas.user import TokenSchema, UserCreate, UserResponse
from app.services.user_service import create_user, logout_user
from app.database import get_db
from app.models.user import User
from app.dependencies import (
    create_access_token,
    create_refresh_token,
    verify_password
)

router = APIRouter()

@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user_endpoint(user: UserCreate, db: Session = Depends(get_db)):
    # Check if user already exists
    if db.query(User).filter_by(nombre_usuario=user.nombre_usuario).first():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User already registered",
        )

    # Create user
    return create_user(db, user)

@router.post("/iniciar-sesion", response_model=TokenSchema, status_code=status.HTTP_201_CREATED)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
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
        "access_token": create_access_token(user.nombre_usuario),
        "refresh_token": create_refresh_token(user.nombre_usuario),
    }
