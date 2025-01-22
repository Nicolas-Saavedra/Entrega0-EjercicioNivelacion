from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserLogin, UserResponse
from app.services.user_service import create_user, login_user, logout_user
from app.database import get_db
from app.models.user import User

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

@router.post("/iniciar-sesion", response_model=str, status_code=status.HTTP_201_CREATED)
def login(user: UserLogin, db: Session = Depends(get_db)):
    token = login_user(db, user)

    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )

    return token


@router.post("/logout", response_model=None, status_code=status.HTTP_204_NO_CONTENT)
def logout(token: str, db: Session = Depends(get_db)):
    if not logout_user(token):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No token found to deauthenticate",
        )
