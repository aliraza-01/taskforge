import pytest
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime,timezone
from fastapi.testclient import TestClient
from app.main import app
from app.db.base import Base
from app.api.dependencies import get_db 
from app.models.project import Project
from app.models.task import Task
from app.models.user import User
from app.security.password import hash_password
load_dotenv()
TEST_DATABASE_URL = os.getenv("TEST_DATABASE_URL")
if not TEST_DATABASE_URL:
    raise RuntimeError("TEST_DATABASE_URL is missing from .env")
test_engine = create_engine(TEST_DATABASE_URL)
TestingSessionLocal = sessionmaker(
    bind=test_engine,
    autoflush=False,
    autocommit=False
)
Base.metadata.create_all(bind=test_engine)
@pytest.fixture(autouse=True)
def clean_test_database():
    Base.metadata.drop_all(bind=test_engine)
    Base.metadata.create_all(bind=test_engine)
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
app.dependency_overrides[get_db] = override_get_db

@pytest.fixture
def test_task():
    db = TestingSessionLocal()
    user = User(
        username="ali",
        email="ali@gmail.com",
        password=hash_password("ali")
    )
    try:
        db.add(user)
        db.commit()
        db.refresh(user)

    # try:
    #     yield user
    # finally:
    #     db.delete(user)
    #     db.commit()
    #     db.close()
        project = Project(
            title = "Ali's Project",
            user_id = user.id,
            created_at=datetime.now(timezone.utc)
        )
        db.add(project)
        db.commit()
        db.refresh(project)
        task=Task(
            title="Ali's Task",
            status="todo",
            priority="high",
            project_id=project.id

        )
        db.add(task)
        db.commit()
        db.refresh(task)
        yield task
    finally:
        db.rollback()
        db.close() 
@pytest.fixture
def another_users_task():
    db = TestingSessionLocal()
    other_user = User(
        username="Sara",
        email="sara_test_unique@example.com",
        password=hash_password("sara")
    )
    try:
        db.add(other_user)
        db.commit()
        db.refresh(other_user) 
        project = Project(
            title = "Sara's Project",
            user_id = other_user.id,
            created_at=datetime.now(timezone.utc)
        )
        db.add(project)
        db.commit()
        db.refresh(project)
        task = Task(
            title="Sara's Task",
            status="todo",
            priority="medium",
            project_id=project.id
        )
        db.add(task)
        db.commit()
        db.refresh(task)
        yield task
    finally:
        db.rollback()
        db.close()
@pytest.fixture
def test_project(test_task):
    db = TestingSessionLocal()
    try:
        user = db.query (User).filter_by(username="ali").first()
        project = Project(
            title ="Ali's Test Project",
            user_id=user.id,
            created_at = datetime.now(timezone.utc)
        )
        db.add(project)
        db.commit()
        db.refresh(project)
        yield project
    finally:
        db.rollback()
        db.close()

@pytest.fixture
def client():
    return TestClient(app)