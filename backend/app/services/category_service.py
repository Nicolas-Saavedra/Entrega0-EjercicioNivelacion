from sqlalchemy.orm import Session
from app.models.category import Category
from app.schemas.category import CategoryCreate, CategoryUpdate

def create_category(db: Session, category_create: CategoryCreate) -> Category:
    db_category = Category(
        nombre=category_create.nombre,
        descripcion=category_create.descripcion
    )
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def update_category(db: Session, category: Category, category_update: CategoryUpdate) -> Category:
    category.nombre = category_update.nombre or category.nombre
    category.descripcion = category_update.descripcion or category.descripcion
    db.commit()
    db.refresh(category)
    return category

def delete_category(db: Session, category: Category) -> None:
    db.delete(category)
    db.commit()
