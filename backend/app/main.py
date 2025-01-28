from fastapi import FastAPI
from app.routers import user as user_router, task as task_router, category as category_router
from app.models import *
from app.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(root_path="/api/v1")

app.include_router(user_router.router, prefix="/usuarios", tags=["users"])
app.include_router(task_router.router, prefix="/tareas", tags=["tasks"])
app.include_router(category_router.router, prefix="/categorias", tags=["categories"])
