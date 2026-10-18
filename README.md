# TaskForge

TaskForge is a task and project management REST API built with FastAPI and PostgreSQL.

## Features

- User registration and JWT authentication
- Task and project CRUD operations
- SQLAlchemy ORM and database relationships
- Alembic database migrations
- Request validation with Pydantic
- Automated tests with pytest
- Docker and Docker Compose support

## Tech Stack

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Alembic
- pytest
- Docker

## Run Locally with Docker

1. Install Docker Desktop.
2. Copy .env.example to .env, then replace the JWT_SECRET_KEY placeholder with a strong random secret.
3. Start the application and database:

   ```bash
   docker compose up --build -d
   ```

4. Create the database tables:

   ```bash
   docker compose exec web alembic upgrade head
   ```

5. Open the API documentation:

   http://localhost:8000/docs

## Stop the Services

```bash
docker compose down
```

The named PostgreSQL volume is preserved by default.

## Testing

Run the tests in your local Python environment:

```bash
python -m pytest -v
```
