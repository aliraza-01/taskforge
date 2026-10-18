from datetime import datetime
from sqlalchemy import String, ForeignKey, Text, TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base

class Project(Base):
    __tablename__ = "projects"
    id : Mapped[int] = mapped_column(primary_key=True)
    title : Mapped[str] = mapped_column(String(100),nullable=False)
    description : Mapped[str | None] = mapped_column(Text)
    created_at : Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True),
        nullable=False
        ) 
    
    user_id : Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False
    )
    user : Mapped["User"] = relationship(back_populates="projects")
    tasks : Mapped[list["Task"]] = relationship(
        back_populates="project"
        , cascade="all,delete-orphan"
    )