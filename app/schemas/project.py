from pydantic import BaseModel,ConfigDict
from datetime import datetime
class ProjectCreate(BaseModel):
    title : str 
    description : str | None = None
    created_at : datetime | None = None
class ProjectResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id : int 
    title : str
    description : str | None = None
    created_at : datetime | None = None
class ProjectUpdate(BaseModel):
    title : str | None = None
    description : str | None = None
    created_at : datetime | None = None


