# Task Management API

A simple **Task Management REST API** built with **FastAPI**, **SQLAlchemy**, **PostgreSQL**, **JWT authentication**, and **Argon2 password hashing**.

The project provides a backend foundation for user registration/authentication and task management.

## Tech Stack

- Python
- FastAPI
- SQLAlchemy
- PostgreSQL
- Pydantic
- JWT
- Argon2 password hashing
- Alembic
- Uvicorn

## Features

- User registration
- User authentication
- Secure password hashing with Argon2
- JWT-based authentication
- Task management API
- PostgreSQL database integration
- SQLAlchemy ORM
- Database migrations with Alembic
- Automatic API documentation through FastAPI

## Project Structure

```text
task_management/
│
├── main.py
├── requirements.txt
├── .env
├── .gitignore
│
└── src/
    ├── tasks/
    │   └── router.py
    │
    ├── user/
    │   └── router.py
    │
    └── utils/
        └── db.py
```

> The exact contents of `src/` may change as the project develops.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/task-management.git
cd task-management
```

### 2. Create a virtual environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in the project root.

Example:

```env
DB_CON=postgresql://username:password@localhost:5432/database_name
SECRET_KEY=your_secret_key
ALGORITHM=HS256
EXP_TIME=30
```

### Important

**Do not upload your real `.env` file to GitHub.**

The `.gitignore` file is configured to ignore `.env`.

If credentials or secret keys have already been committed to Git, rotate them before making the repository public.

## Database Setup

Make sure PostgreSQL is installed and running.

Create a PostgreSQL database and update `DB_CON` in your `.env` file.

Example:

```env
DB_CON=postgresql://postgres:password@localhost:5432/task_management
```

The application uses SQLAlchemy to create the required database tables.

## Run the Application

Start the FastAPI server with:

```bash
uvicorn main:app --reload
```

The API will normally be available at:

```text
http://127.0.0.1:8000
```

## API Documentation

FastAPI automatically provides interactive API documentation.

### Swagger UI

Open:

```text
http://127.0.0.1:8000/docs
```

### ReDoc

Open:

```text
http://127.0.0.1:8000/redoc
```

You can use Swagger UI to test the API endpoints directly from your browser.

## Example User Registration

Example request body:

```json
{
  "name": "Alice Johnson",
  "username": "alice",
  "password": "alice123",
  "email": "alice@example.com"
}
```

Another example:

```json
{
  "name": "Bob Smith",
  "username": "bob",
  "password": "bob123",
  "email": "bob@example.com"
}
```

> These are example credentials for testing only. Use strong passwords in a real application.

## Root Endpoint

The project currently includes a basic root endpoint:

```http
GET /
```

Expected response:

```text
working
```

## Authentication

The project is designed to use:

- JWT for authentication tokens
- Argon2 for password hashing
- Environment variables for secrets and configuration

Passwords should never be stored as plain text in a production database.

## Development

Run the server in development mode:

```bash
uvicorn main:app --reload
```

After making code changes, FastAPI/Uvicorn will automatically reload the development server.

## Future Improvements

- Add task creation, update, and deletion endpoints
- Add task status and priority
- Add due dates
- Add user-specific task authorization
- Add refresh tokens
- Add pagination and filtering
- Add automated tests
- Improve exception handling
- Add Docker support
- Add CI/CD with GitHub Actions
- Deploy the API to a cloud platform

## License

This project is currently for learning and development purposes.
