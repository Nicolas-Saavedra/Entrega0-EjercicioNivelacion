from datetime import datetime
from typing import List
from pydantic import BaseModel
from .task import TaskSchema

class UserCreate(BaseModel):
    nombre_usuario: str
    contrasenia: str

class UserLogin(UserCreate):
    pass

class UserTasksResponse(BaseModel):
    tasks: List[TaskSchema]

class TokenSchema(BaseModel):
    access_token: str
    refresh_token: str

class RefreshTokenSchema(BaseModel):
    access_token: str
    refresh_token: str

class AccessTokenSchema(BaseModel):
    access_token: str
    refresh_token: str

class TokenPayload(BaseModel):
    exp: datetime
    sub: str

class UserSchema(BaseModel):
    id: int
    nombre_usuario: str
    imagen_perfil: str

    class Config:
        orm_mode = True  # To work seamlessly with SQLAlchemy models
