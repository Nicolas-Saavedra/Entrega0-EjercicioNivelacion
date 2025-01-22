from datetime import datetime
from pydantic import BaseModel

class TaskCreate(BaseModel):
    texto_tarea: str
    fecha_creacion: datetime
    fecha_tentativa_finalizacion: datetime | None
    estado: str
    id_Usuario: int
    id_Categoria: int


class TaskCreateResponse(BaseModel):
    id: int
    texto_tarea: str
    fecha_creacion: datetime
    fecha_tentativa_finalizacion: datetime | None
    estado: str
    id_Usuario: int
    id_Categoria: int

    """
class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    texto_tarea: Mapped[str] = mapped_column(String, index=True)
    fecha_creacion: Mapped[datetime] = mapped_column(DateTime, index=True)
    fecha_tentativa_finalizacion: Mapped[datetime] = mapped_column(DateTime, index=True)
    estado: Mapped[str] = mapped_column(String, index=True)
    id_Usuario: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    id_Categoria: Mapped[int] = mapped_column(Integer, ForeignKey("categories.id"))
        """
