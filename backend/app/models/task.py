from sqlalchemy import Column, Integer, String, Date, ForeignKey
from app.database import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    texto_tarea = Column(String, index=True)
    fecha_creacion = Column(Date, index=True)
    fecha_tentativa_finalizacion = Column(Date, index=True)
    estado = Column(String, index=True)
    id_Usuario = Column(Integer, ForeignKey("users.id"))
    id_Categoria = Column(Integer, ForeignKey("categories.id"))
