# TaskForge — Task & Project Management API

**A RESTful backend for managing projects, tasks, and users, built with FastAPI and PostgreSQL.**

TaskForge is a task and project management API inspired by platforms such as Trello and Jira. It provides endpoints for organizing projects, managing tasks, and handling user authentication.

This project demonstrates practical backend development concepts, including REST API design, database relationships, authentication, request validation, automated testing, database migrations, and containerization.

## Features

- **User Management** — Register users and manage user-related operations.
- **JWT Authentication** — Protect authorized endpoints using token-based authentication.
- **Project Management** — Create, retrieve, and delete projects.
- **Task Management** — Create, retrieve, update, and delete tasks.
- **Request Validation** — Validate incoming data with Pydantic and return appropriate validation errors.
- **Relational Database** — Use SQLAlchemy ORM with PostgreSQL to manage data and model relationships between users, projects, and tasks.
- **Database Migrations** — Manage database schema changes using Alembic.
- **Automated Testing** — Test application behavior using pytest.
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

TaskForge follows a layered backend structure that separates responsibilities and makes the application easier to maintain.

- **API Layer** — Defines endpoints and handles HTTP requests and responses.
- **Schema Layer** — Validates incoming data and structures API responses.
- **Service Layer** — Contains business logic and database operations.
- **Model Layer** — Defines database tables and relationships.
- **Database Layer** — Manages database sessions and communication with PostgreSQL.
- **Security Layer** — Supports password handling, token creation, and authentication.

## Getting Started

### Prerequisites

Install the following tools before running the project:

- [Git](https://git-scm.com/)
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) with Docker Compose
- A code editor such as [Visual Studio Code](https://code.visualstudio.com/)

### 1. Clone the Repository

```bash
git clone https://github.com/aliraza-01/taskforge.git
cd taskforge
```

### 2. Configure Environment Variables

Create a local `.env` file using `.env.example` as a template. Set the required database connection values and a strong, private JWT secret according to the application's configuration.

Keep your `.env` file and all private credentials out of version control. Never publish production secrets to GitHub.

### 3. Build and Start the Services

From the project root directory, run:

```bash
docker compose up --build -d
```

This builds the application image if needed and starts the API and database services in the background.

To check their status, run:

```bash
docker compose ps
```

### 4. Apply Database Migrations

Run the following command to apply the database migrations:

```bash
docker compose exec web alembic upgrade head
```

This updates the database schema to the latest available Alembic revision. Make sure the services are running before executing the command.

### 5. Open the API Documentation

Once the application is running, visit:

[**http://localhost:8000/docs**](http://localhost:8000/docs)

Use Swagger UI to explore the available endpoints, submit requests, and review API responses.

## Running Tests

To run the automated tests in your local Python environment, activate your virtual environment and install the project's dependencies. Then run:

```bash
python -m pytest -v
```

The `-v` option displays individual test names and their results.

## Stopping the Services

To stop the Docker Compose services, run:

```bash
docker compose down
```

This stops and removes the Compose containers and network. Named database volumes are preserved by default, so your database data can remain available when you start the services again.

## What I Learned

Building TaskForge provided hands-on experience with:

- Designing RESTful API endpoints and using appropriate HTTP status codes.
- Implementing JWT-based authentication and authorization.
- Modeling relational data and relationships with SQLAlchemy.
- Validating requests and handling common API errors.
- Managing database schema changes with Alembic.
- Writing and executing automated tests with pytest.
- Running multi-container applications with Docker Compose.
- Using Git and GitHub for version control and project collaboration.

## Future Improvements

Potential improvements include:

- Deploying the API to a cloud hosting platform.
- Adding continuous integration and automated test execution.
- Improving logging, monitoring, and production configuration.
- Expanding API functionality and test coverage.

---

**TaskForge is a practical backend portfolio project demonstrating hands-on skills in Python API development, relational databases, authentication, testing, and containerized applications.**