from app.db.session import SessionLocal
from app.services.task_service import create_task
from app.schemas.task import TaskCreate
task_data = TaskCreate(
    project_id=1,
    title = "Build API",
    description="Create task endpoint",
    status = "todo",
    priority= "high",
    deadline= None
)
print(task_data)
print(task_data.title)
print(task_data.project_id)

# with SessionLocal() as db:

#     task = create_task(
#         db,
#         project_id=1,
#         title="Build API",
#         description="Create the first API task",
#         status="todo",
#         priority="high",
#         deadline=None
#     )

#     print(task.id)
#     print(task.title)
#     print(task.status)
#      print(task.priority)
class Student:
    def __init__(self,name):
        self.name = name
s1 = Student("nasir")
print(s1)
print(s1.name)