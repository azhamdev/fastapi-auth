from app.models.database import User
from app.modules.auth.utils import hash_password, is_password_valid
from sqlmodel import Session, select
from app.models.engine import db_session
from app.modules.auth.schema import RegisterUser, LoginUser
from fastapi import APIRouter, Depends, HTTPException, status

auth_router = APIRouter(prefix="/auth", tags=["Auth"])


@auth_router.post("/register")
def register_user(body: RegisterUser, db: Session = Depends(db_session)):
    hashed_password = hash_password(body.password)
    new_user=User(name=body.name, email=body.email, password=hashed_password)

    db.add(new_user)
    db.commit()
    return {"message": "User registered successfully"}


@auth_router.post("/login")
def login_user(body: LoginUser, db: Session = Depends(db_session)):
    user = db.exec(select(User).where(User.email == body.email)).first()
    if not user:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="User not found")

    if not is_password_valid(body.password, user.password):
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    return {"message": "Login successfuly"}
