from app.models.project import Project
from sqlalchemy.orm import Session
from sqlalchemy import Select
from app.schemas.project import ProjectUpdate
from app.models.user import User
def create_project(db:Session,user_id,title,description,created_at):
    project = Project(
        user_id = user_id,
        title = title,
        description = description,
        created_at = created_at
    )
    db.add(project)
    db.commit()
    db.refresh(project)
    return project
def get_project(db:Session,current_user,project_id):
    result = db.execute(
        Select(Project).where(Project.id==project_id)
    )
    project = result.scalar_one_or_none()
    if project is None:
        return None
    if current_user.id == project.user_id:
        return project
    return None
def get_projects(db:Session,curren_user):
    result = db.execute(
        Select(Project).where(curren_user.id==Project.user_id)
    )
    projects = result.scalars().all()
    return projects
def update_project(project_id,current_user, project_update_data:ProjectUpdate,db:Session):
    result = db.execute(
        Select(Project).where(Project.id==project_id)
    )

    project = result.scalar_one_or_none()
    if project is None:
        return None
    if current_user.id == project.user_id:

        updated_project = project_update_data.model_dump(exclude_unset=True)
        for field,value in updated_project.items():
            setattr(project,field,value)
        db.commit()
        db.refresh(project)
        return project
    return None
def delete_project(project_id,current_user,db:Session):
    result = db.execute(
        Select(Project).where(Project.id==project_id)
    )
    project = result.scalar_one_or_none()
    if project is None:
        return None
    if current_user.id == project.user_id:
        db.delete(project)
        db.commit()
        return project
    return None
