from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.category import CategoryCreate, CategorySchema
from app.models.category import Category
from app.database import get_db
from app.dependencies import get_current_user
from app.services.category_service import create_category

router = APIRouter()

@router.post("/", response_model=CategorySchema, status_code=status.HTTP_201_CREATED)
def create_category_endpoint(category: CategoryCreate, _: User = Depends(get_current_user), db: Session = Depends(get_db)):
    if db.query(Category).filter_by(nombre=category.nombre).first():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Category already exists",
        )
    return create_category(db, category)
