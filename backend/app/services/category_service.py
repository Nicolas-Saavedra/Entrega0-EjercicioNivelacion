from sqlalchemy.orm import Session
from app.models.category import Category
from app.schemas.category import CategoryCreate

def create_category(db: Session, category: CategoryCreate) -> Category:
    db_category = Category(
        nombre=category.nombre,
        descripcion=category.descripcion
    )
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category
