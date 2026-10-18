from sqlalchemy.orm import Session
from sqlalchemy import Select
from app.models.project import Project
from app.models.task import Task
from app.schemas.task import TaskUpdate


def create_task(db:Session,project_id,title,description,status,priority,deadline,current_user):
    task = Task(
        project_id = project_id,
        title = title,
        description = description,
        status = status,
        priority = priority,
        deadline = deadline,
        
    )
    result = db.execute(
        Select(Project).where(Project.id==task.project_id)
    )
    project = result.scalar_one_or_none()
    if project is None:
        return None
    if current_user.id == project.user_id:
        db.add(task)
        db.commit()
        db.refresh(task)
        return task
    return None
def get_tasK(db:Session,current_user,task_id:int):
    result = db.execute(
        Select(Task).where(Task.id==task_id)
    )
    task = result.scalar_one_or_none()
    if task is None:
        return None
    result = db.execute(
        Select(Project).where(Project.id==task.project_id)
    )
    project = result.scalar_one_or_none()
    if project is None:
        return project
    if current_user.id == project.user_id:
        return task
    
    return None
def get_tasks(db:Session,current_user):
    result = db.execute(
        Select(Task)
        .join(Project, Task.project_id==Project.id)
        .where(Project.user_id==current_user.id)
    )
    tasks = result.scalars().all()
    return tasks
        
    
def update_task(task_id:int,current_user, task_data:TaskUpdate,db:Session):
    result = db.execute(
        Select(Task).where(Task.id==task_id)
    )
    task = result.scalar_one_or_none()
    if task is None:
        return None
    result = db.execute(
        Select(Project).where(Project.id==task.project_id)
    )
    project = result.scalar_one_or_none()
    if project is None:
        return None
    if current_user.id == project.user_id:
        updates = task_data.model_dump(exclude_unset=True)
        for field,value in updates.items():
            setattr(task,field,value)
        db.commit()
        db.refresh(task)
        return task 
def delete_task(task_id:int,current_user, db:Session):
    result = db.execute(
        Select(Task).where(Task.id==task_id)
    )
    task=result.scalar_one_or_none()
    if task is None:
        return None
    result = db.execute(
        Select(Project).where(Project.id==task.project_id)
    )
    project = result.scalar_one_or_none()
    if project is None:
        return None
    if current_user.id == project.user_id:
        db.delete(task)
        db.commit()
        return task