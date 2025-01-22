from fastapi import FastAPI
from app.routers import user, task, category

app = FastAPI()

app.include_router(user.router, prefix="/users", tags=["users"])
app.include_router(task.router, prefix="/products", tags=["products"])
app.include_router(category.router, prefix="/products", tags=["products"])
