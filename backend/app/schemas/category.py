from pydantic import BaseModel

class CategoryCreate(BaseModel):
    nombre: str
    descripcion: str


class CategorySchema(BaseModel):
    id: str
    nombre: str
    descripcion: str

    class Config:
        orm_mode = True  # To work seamlessly with SQLAlchemy models
