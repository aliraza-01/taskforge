from datetime import datetime
from sqlalchemy import String,ForeignKey, Text, TIMESTAMP, CheckConstraint
from sqlalchemy.orm import Mapped,mapped_column,relationship
from app.db.base import Base

class Task(Base):
    __tablename__ = "tasks"
    id : Mapped[int] = mapped_column(primary_key=True)
    title : Mapped[str] = mapped_column(String(150),nullable=False)
    description : Mapped[str | None] = mapped_column(Text)
    status : Mapped[str] = mapped_column(String(20),nullable=False)
    priority : Mapped[str] = mapped_column(String(10),nullable=False)
    deadline : Mapped[datetime | None] = mapped_column(TIMESTAMP(timezone=True),nullable=True)
    __table_args__ = (
    CheckConstraint(
        "status IN ('todo', 'in_progress', 'completed')",
        name="check_task_status"
    ),
    CheckConstraint(
        "priority IN ('low', 'medium', 'high')",
        name="check_task_priority"
    ),
    )
    project_id : Mapped[int] = mapped_column(
        ForeignKey("projects.id"),
        nullable=False
    )
    project : Mapped["Project"] = relationship(back_populates="tasks")
    

