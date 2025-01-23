from typing import List
from pydantic import BaseModel

class CategoryCreate(BaseModel):
    nombre: str
    descripcion: str

class CategoryUpdate(BaseModel):
    nombre: str | None
    descripcion: str | None

class CategorySchema(BaseModel):
    id: int
    nombre: str
    descripcion: str

    class Config:
        orm_mode = True  # To work seamlessly with SQLAlchemy models

class CategoriesResponse(BaseModel):
    categories: List[CategorySchema]

    class Config:
        orm_mode = True  # To work seamlessly with SQLAlchemy models
