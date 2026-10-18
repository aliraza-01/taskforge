from pydantic import BaseModel,ConfigDict
from datetime import datetime
from typing import Literal

class TaskCreate(BaseModel):
    project_id : int
    title : str
    description : str | None = None
    status : Literal["todo","in_progress","completed"]
    priority : str
    deadline : datetime | None = None
class TaskResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id : int
    project_id : int
    title : str
    description : str | None = None
    status : str
    priority : str
    deadling : datetime | None = None
class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    status: Literal["todo","in_progress","completed"] | None = None
    priority: str | None = None
    deadline: datetime | None = None