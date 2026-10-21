from sqlalchemy import create_engine
from app.core.config import settings
from sqlalchemy.orm import sessionmaker
database_url = settings.neon_database_url or settings.database_url
engine = create_engine(database_url)
SessionLocal = sessionmaker(
    bind = engine,
    autoflush = False,
    # automcommit = False,
)