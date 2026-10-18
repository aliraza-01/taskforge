from pydantic import BaseModel,ConfigDict
class UserCreate(BaseModel):
    username : str
    email : str
    password : str
class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    username : str
    email : str
class UserLoginResponse(BaseModel):
    token : str
    user : UserResponse


class UserUpdate(BaseModel):
    username : str | None = None
    email : str | None = None 
class UserLogin(BaseModel):
    username : str
    password : str