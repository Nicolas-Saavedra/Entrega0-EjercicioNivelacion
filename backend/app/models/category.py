from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base

class Category(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    nombre: Mapped[str] = mapped_column(String, index=True)
    descripcion: Mapped[str] = mapped_column(String, index=False)
    tasks = relationship(
        "Task", back_populates="categoria", cascade="all, delete-orphan"
    )
