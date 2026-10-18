from app.db.session import SessionLocal
import jwt
from fastapi import Depends,HTTPException
from sqlalchemy.orm import Session
from fastapi.security import HTTPBearer
from app.security.token import verify_token
from sqlalchemy import Select
from app.models.user import User
Oauth2_scheme = HTTPBearer()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
def get_current_user(db:Session = Depends(get_db),credentials = Depends(Oauth2_scheme)):
    token = credentials.credentials
    try:
        playload = verify_token(token)
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401,detail="Invalid token")
    user_id = int(playload["sub"])
    result = db.execute(
        Select(User).where(User.id==user_id)
    )
    user = result.scalar_one_or_none()
    if user is None:
        raise HTTPException(status_code=401,detail="User not found")
    return user

    


