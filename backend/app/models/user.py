from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    nombre_usuario: Mapped[str] = mapped_column(String, index=True, unique=True)
    contrasenia: Mapped[str] = mapped_column(String, index=True)
    imagen_perfil: Mapped[str] = mapped_column(String, index=False)
