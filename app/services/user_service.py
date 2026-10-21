from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserUpdate
from sqlalchemy.exc import IntegrityError
from app.security.password import hash_password,verify_password
from fastapi import HTTPException
def create_user(db:Session,username,email,password):
    existing_user = db.scalar(
        select(User).where(User.email==email)
    )
    if existing_user:
        raise HTTPException(status_code=409,detail="Email is already registered")
    user = User(
        username=username,
        email=email,
        password=hash_password(password)
    )
    try:
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
    except IntegrityError:
        db.rollback()
        raise
def get_user(user_id,db:Session):
    result = db.execute(select(User).where(User.id==user_id))
    user = result.scalar_one_or_none()
    return user
def update_user(user_id,update_user_data:UserUpdate,db:Session):
    result = db.execute(select(User).where(User.id==user_id))
    user = result.scalar_one_or_none()
    if user is None:
        return None
    updated_user = update_user_data.model_dump(exclude_unset=True)
    for field,value in updated_user.items():
        setattr(user,field,value)
    db.commit()
    db.refresh(user)
    return user
def delete_user(user_id,db:Session):
    result = db.execute(select(User).where(User.id==user_id))
    user = result.scalar_one_or_none()
    if user is None:
        return None
    db.delete(user)
    db.commit()
    return user
def verify_user(user_verify_data,db:Session):
    result = db.execute(
        select(User).where(User.username==user_verify_data.username)
    )
    user = result.scalar_one_or_none()
    if user is None:
        raise HTTPException(status_code=404,detail="User not found")

    password = verify_password(user_verify_data.password,user.password)
    if password:
        return user
    else:
        return None


    
    


