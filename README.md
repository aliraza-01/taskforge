# TaskForge — Task & Project Management API

**A RESTful backend for managing projects, tasks, and users, built with FastAPI and PostgreSQL.**

TaskForge is a backend project inspired by task management platforms such as Trello and Jira. It provides API endpoints for organizing projects, managing tasks, and handling user authentication.

The project demonstrates practical backend development concepts, including REST API design, database relationships, authentication, request validation, automated testing, and containerization.

## Features

- **User Management** — Register users and manage user-related operations.
- **JWT Authentication** — Protect authorized endpoints using token-based authentication.
- **Project Management** — Create, retrieve, and delete projects.
- **Task Management** — Create, retrieve, update, and delete tasks.
- **Request Validation** — Validate incoming data with Pydantic and return appropriate validation errors.
- **Relational Database** — Use SQLAlchemy ORM to work with PostgreSQL and model relationships between users, projects, and tasks.
- **Database Migrations** — Manage database schema changes with Alembic.
- **Automated Testing** — Verify application behavior using pytest.
- **Docker Support** — Run the API and PostgreSQL database using Docker Compose.
- **Interactive API Documentation** — Explore and test endpoints through Swagger UI.

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| FastAPI | REST API development |
| PostgreSQL | Relational database |
| SQLAlchemy | ORM and database operations |
| Pydantic | Request validation and data schemas |
| Alembic | Database migrations |
| JWT | Token-based authentication |
| pytest | Automated testing |
| Docker & Docker Compose | Containerization and service management |

## Architecture Overview

The application follows a layered backend structure:

- **API layer:** Defines endpoints and handles HTTP requests.
- **Schema layer:** Validates incoming data and structures responses.
- **Service layer:** Contains business logic and database operations.
- **Model layer:** Defines database tables and relationships.
- **Database layer:** Connects the application to PostgreSQL.
- **Security layer:** Supports password handling and JWT authentication.

This structure helps separate responsibilities and makes the application easier to maintain and extend.

## Getting Started

### Prerequisites

- Git
- Docker Desktop with Docker Compose
- A code editor such as VS Code

### 1. Clone the repository

```bash
git clone https://github.com/aliraza-01/taskforge.git
cd taskforge
```

Replace the placeholder with your actual GitHub repository URL.

### 2. Configure environment variables

Create your local environment file using `.env.example` as a template. Set the required database connection values and a strong, private JWT secret according to your application's configuration.

Do not commit private credentials or production secrets to the repository.

### 3. Build and start the services

```bash
docker compose up --build -d
```

This builds the application image and starts the services in the background.

### 4. Apply database migrations

```bash
docker compose exec web alembic upgrade head
```

Replace `<API_SERVICE_NAME>` with the actual API service name defined in your Compose file.

### 5. Open the API documentation

Once the application is running, visit:

**http://localhost:8000/docs**

Use Swagger UI to inspect endpoints, submit requests, and review API responses.

## Running Tests

To run the automated tests in your local Python environment, activate your virtual environment, install the project dependencies, and run:

```bash
python -m pytest -v
```

The `-v` option displays the individual test names and their results.

## Stopping the Services

```bash
docker compose down
```

This stops and removes the Compose containers and network. Named database volumes are preserved by default unless you explicitly remove them.

## What I Learned

Building TaskForge provided hands-on practice with:

- Designing RESTful endpoints and HTTP response codes.
- Implementing authentication and authorization.
- Modeling relational data with SQLAlchemy.
- Validating requests and handling common API errors.
- Managing database schema changes with Alembic.
- Writing and running automated tests with pytest.
- Running multi-container applications with Docker Compose.
- Using Git and GitHub to track and publish code changes.

## Future Improvements

Potential next steps include production deployment, continuous integration, improved monitoring, and additional API features.

---

**TaskForge is a practical backend portfolio project demonstrating core skills in Python API development, relational databases, testing, and containerized applications.**
