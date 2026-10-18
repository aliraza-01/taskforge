from sqlalchemy import text
from app.db.session import engine
from app.db.session import SessionLocal
db = SessionLocal()
print("Session Created")
db.close()
# with engine.connect() as connection:
#     result = connection.execute(text("SELECT 1"))
#     print(result.scalar())
