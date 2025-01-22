from datetime import datetime
from pydantic import BaseModel

class UserCreate(BaseModel):
    nombre_usuario: str
    contrasenia: str

class UserLogin(UserCreate):
    pass

class TokenSchema(BaseModel):
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
