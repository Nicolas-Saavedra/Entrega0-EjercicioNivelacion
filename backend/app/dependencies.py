from datetime import datetime
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, exceptions
from pydantic import ValidationError
from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import TokenPayload, UserSchema
from app.database import get_db
from app.utils import (
    ALGORITHM,
    JWT_SECRET_KEY
)

reuseable_oauth = OAuth2PasswordBearer(
    tokenUrl="/usuarios/iniciar-sesion",
    scheme_name="JWT"
)

async def get_current_user(token: str = Depends(reuseable_oauth), db: Session = Depends(get_db)) -> UserSchema:
    try:
        payload = jwt.decode(
            token, JWT_SECRET_KEY, algorithms=[ALGORITHM]
        )
        token_data = TokenPayload(**payload)

        # TODO: Errors here are never caught properly, decoding already catches expirations
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

    user = db.query(User).filter(User.id == token_data.sub).first()

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Could not find user",
        )

    return user
