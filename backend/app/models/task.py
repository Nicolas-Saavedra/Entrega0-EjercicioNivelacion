from datetime import datetime
from sqlalchemy import DateTime, Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base

class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    texto_tarea: Mapped[str] = mapped_column(String, index=True)
    fecha_creacion: Mapped[datetime] = mapped_column(DateTime, index=True)
    fecha_tentativa_finalizacion: Mapped[datetime] = mapped_column(DateTime, index=True)
    estado: Mapped[str] = mapped_column(String, index=True)
    id_Usuario: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    id_Categoria: Mapped[int] = mapped_column(Integer, ForeignKey("categories.id"))
