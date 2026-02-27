from app.models.database import User
from app.modules.auth.utils import validate_token
from app.models.engine import db_session
from sqlmodel import Session
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer

security = HTTPBearer()

def get_current_user(token=Depends(dependency=security), db:Session = Depends(db_session)):
    current_user = validate_token(token.credentials)
    if not current_user:
        raise HTTPException(401, "Invalid token")
    
    user = db.get(User, current_user.get("id"))
    if not user:
        raise HTTPException(404, "User not found")
    
    return user
    

