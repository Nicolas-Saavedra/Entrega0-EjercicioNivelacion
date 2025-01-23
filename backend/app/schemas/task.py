from datetime import datetime
from pydantic import BaseModel
from .category import CategorySchema

class TaskCreate(BaseModel):
    texto_tarea: str
    fecha_creacion: datetime
    fecha_tentativa_finalizacion: datetime | None
    estado: str
    id_Usuario: int
    id_Categoria: int

class TaskUpdate(BaseModel):
    texto_tarea: str | None
    estado: str | None

class TaskSchema(BaseModel):
    id: int
    texto_tarea: str
    fecha_creacion: datetime
    fecha_tentativa_finalizacion: datetime | None
    estado: str
    id_Usuario: int
    id_Categoria: int
    categoria: CategorySchema

    class Config:
        orm_mode = True  # To work seamlessly with SQLAlchemy models
