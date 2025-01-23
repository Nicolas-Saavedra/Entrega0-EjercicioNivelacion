from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.category import CategoriesResponse, CategoryCreate, CategorySchema, CategoryUpdate
from app.models.category import Category
from app.database import get_db
from app.dependencies import get_current_user
from app.services.category_service import create_category, delete_category, update_category

router = APIRouter()


@router.get("/", response_model=CategoriesResponse, status_code=status.HTTP_200_OK)
def get_all_categories_endpoint(_: User = Depends(get_current_user), db: Session = Depends(get_db)):
    return {
        "categories": db.query(Category).all()
    }

@router.post("/", response_model=CategorySchema, status_code=status.HTTP_201_CREATED)
def create_category_endpoint(category_create: CategoryCreate, _: User = Depends(get_current_user), db: Session = Depends(get_db)):
    if db.query(Category).filter_by(nombre=category_create.nombre).first():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Category with that name already exists",
        )
    return create_category(db, category_create)

@router.put("/{id}", response_model=CategorySchema, status_code=status.HTTP_200_OK)
def update_category_endpoint(id: str, category_update: CategoryUpdate, _: User = Depends(get_current_user), db: Session = Depends(get_db)):
    category = db.query(Category).filter_by(id=id).first()
    if not category:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Category does not exist",
        )
    if not (category_update.nombre or category_update.descripcion):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Empty request"
        )
    return update_category(db, category, category_update)

@router.delete("/{id}", response_model=None, status_code=status.HTTP_204_NO_CONTENT)
def delete_category_endpoint(id: str, _: User = Depends(get_current_user), db: Session = Depends(get_db)):
    category = db.query(Category).filter_by(id=id).first()
    if not category:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Category does not exist",
        )
    return delete_category(db, category)
