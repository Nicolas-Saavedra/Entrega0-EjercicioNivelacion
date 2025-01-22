from sqlalchemy import Column, Integer, String
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    nombre_usuario = Column(String, index=True, unique=True)
    contrasenia = Column(String, index=True)
    imagen_perfil = Column(String, index=True)
