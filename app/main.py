from fastapi import FastAPI,Depends,HTTPException,status
from sqlalchemy import text
from sqlalchemy.orm import Session
from app.api.dependencies import get_db,get_current_user
from app.schemas.task import TaskCreate,TaskResponse,TaskUpdate
from app.schemas.project import ProjectCreate,ProjectResponse,ProjectUpdate
from app.schemas.user import UserCreate,UserResponse,UserUpdate,UserLogin,UserLoginResponse
from app.services.task_service import create_task,get_tasK,get_tasks,update_task,delete_task
from app.services.project_service import create_project,get_project,update_project,delete_project,get_projects
from app.services.user_service import create_user,get_user,update_user,delete_user,verify_user
from fastapi.responses import RedirectResponse
from app.security.token import create_token
app = FastAPI()
@app.get("/test-db")
def test_db(db:Session=Depends(get_db)):
    result = db.execute(text("SELECT 1"))
    return {"database" : result.scalar()==1}
@app.get("/",include_in_schema=False)
async def root():
    return RedirectResponse(url="/docs")
@app.post("/tasks",response_model=TaskResponse,status_code=201)
def create_task_endpoint(task_data:TaskCreate, current_user=Depends(get_current_user),db:Session=Depends(get_db)):

    task = create_task(
        db,
        project_id=task_data.project_id,
        title=task_data.title,
        description=task_data.description,
        status=task_data.status,
        priority=task_data.priority,
        deadline=task_data.deadline,
        current_user=current_user

    )
    if task is None:
        raise HTTPException(status_code=404,detail="Project Not found")
    return task

@app.get("/tasks",response_model=list[TaskResponse])
def get_all_tasks(current_user=Depends(get_current_user),db:Session=Depends(get_db)):
    tasks = get_tasks(db,current_user)
    if tasks is None:
        raise HTTPException(status_code=404,detail="Tasks not found")
    return tasks
@app.get("/tasks/{task_id}",response_model=TaskResponse)
def get_task_endpoint(task_id:int,db:Session = Depends(get_db),current_user=Depends(get_current_user)):
    task = get_tasK(db,current_user,task_id)
    if task is None:
        raise HTTPException(status_code=404,detail="Task not found")
    return task
@app.patch("/tasks/{task_id}",response_model=TaskResponse)
def update_task_endpoint(task_id:int ,task_data : TaskUpdate, current_user=Depends(get_current_user), db:Session=Depends(get_db)):
    task = update_task(task_id, current_user, task_data, db)
    if task is None:
        raise HTTPException(status_code=404,detail="Task not found.")
    return task
@app.delete("/tasks/{task_id}",response_model=TaskResponse)
def delete_task_endpoint(task_id:int,current_user=Depends(get_current_user),db:Session=Depends(get_db)):
    task = delete_task(task_id,current_user,db)
    if task is None:
        raise HTTPException(status_code=404,detail="Task not found")
    return task
@app.post("/projects",response_model=ProjectResponse,status_code=201)
def create_project_endpoint(project_data:ProjectCreate,db:Session=Depends(get_db),current_user=Depends(get_current_user)):
    project = create_project(
        db,

        user_id=current_user.id,
        title=project_data.title,
        description=project_data.description,
        created_at = project_data.created_at
    )
    return project 

@app.get("/projects/{project_id}",response_model=ProjectResponse)
def get_project_endpoint(project_id:int,current_user=Depends(get_current_user),db:Session=Depends(get_db)):
    project = get_project(db,current_user,project_id)
    if project is None:
        raise HTTPException(status_code=404,detail="Project not Found")
    return project
@app.get("/projects",response_model=list[ProjectResponse])
def get_all_project_endpoint(current_user=Depends(get_current_user),db:Session=Depends(get_db)):
    projects = get_projects(db,current_user)
    if projects is None:
        raise HTTPException(status_code=404,detail="Project not found")
    return projects
@app.patch("/projects/{project_id}",response_model=ProjectResponse)
def update_project_endpoint(project_id:int,project_data_update:ProjectUpdate, current_user=Depends(get_current_user), db:Session=Depends(get_db)):
    project = update_project(project_id,current_user, project_data_update,db)
    if project is None:
        raise HTTPException(status_code=404,detail="Project not Found")
    return project
@app.delete("/projects/{project_id}",response_model=ProjectResponse)
def delete_project_endpoint(project_id:int,current_user=Depends(get_current_user),db:Session=Depends(get_db)):
    project = delete_project(project_id,current_user,db)
    if project is None:
        raise HTTPException(status_code=404,detail="Project not Found")
    return project

@app.post("/users",response_model=UserResponse,status_code=status.HTTP_201_CREATED)
def create_user_endpoint(user_data:UserCreate,db:Session=Depends(get_db)):
    user = create_user(
        db,
        username = user_data.username,
        email = user_data.email,
        password=user_data.password

    )
    return user
@app.get("/users/me",response_model=UserResponse)
def get_me(current_user=Depends(get_current_user)):
    return current_user

@app.get("/users/{user_id}",response_model=UserResponse)
def get_user_endpoint(user_id:int,db:Session=Depends(get_db)):
    user = get_user(user_id,db)
    if user is None:
        raise HTTPException(status_code=404,detail="User not found")
    return user
@app.patch("/users/{user_id}",response_model=UserUpdate)
def update_user_endpoint(user_id:int,update_user_data:UserUpdate, db:Session=Depends(get_db)):
    user = update_user(user_id,update_user_data,db)
    if user is None:
        raise HTTPException(status_code=404,detail="User not found")
    return user
@app.delete("/users/{user_id}",response_model=UserResponse)
def delete_user_endpoint(user_id:int,db:Session=Depends(get_db)):
    user = delete_user(user_id,db)
    if user is None:
        raise HTTPException(status_code=404,detail="User not found")
    return user
@app.post("/login",response_model=UserLoginResponse)
def user_verify_endpoint(user_verify_data:UserLogin,db:Session=Depends(get_db)):
    user = verify_user(user_verify_data,db)
    if user:
        token = create_token(user.id)
        return {
            "token" : token,
            "user" : user
        }

    
    raise HTTPException(status_code=401, detail="Invalid username or password")
@app.post("/login",response_model=UserResponse)
def get_user(user_login_data:UserLogin,db:Session=Depends(get_db)):
    user = create_user
    if user is not None:
        raise HTTPException(status_code=404,detail="User already exists")
