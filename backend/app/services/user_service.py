from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate 
from app.utils import get_hashed_password 
from hashlib import md5 

def create_user(db: Session, user: UserCreate) -> User:
    hashed_password = get_hashed_password(user.contrasenia)  # Example password hashing
    hashed_username = md5(user.nombre_usuario.encode()).hexdigest()
    db_user = User(
        nombre_usuario=user.nombre_usuario,
        contrasenia=hashed_password,
        imagen_perfil=f"https://www.gravatar.com/avatar/{hashed_username}?d=identicon&s=200",
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
