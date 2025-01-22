from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate, UserLogin
from app.dependencies import create_token, delete_token
from hashlib import md5, sha256

def create_user(db: Session, user: UserCreate) -> User:
    hashed_password = sha256(user.contrasenia.encode()).hexdigest()  # Example password hashing
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

def login_user(db: Session, user: UserLogin) -> str | None:
    hashed_password = sha256(user.contrasenia.encode()).hexdigest()  # Example password hashing
    db_user = db.query(User).filter_by(nombre_usuario=user.nombre_usuario).first()

    if db_user and db_user.contrasenia == hashed_password:
        return create_token(db_user.nombre_usuario)
    else:
        return None

def logout_user(token: str) -> bool:
    return bool(delete_token(token))
