from fastapi import FastAPI
from app.routers import user, task, category
from app.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user.router, prefix="/usuarios", tags=["users"])
app.include_router(task.router, prefix="/tareas", tags=["tasks"])
app.include_router(category.router, prefix="/categorias", tags=["categories"])
