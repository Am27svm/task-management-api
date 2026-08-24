# Task Management API

A backend **Task Management API** built with **FastAPI**, **SQLAlchemy**, and **PostgreSQL**. The project follows a modular structure with separate modules for users, tasks, database utilities, controllers, DTOs, models, and routes.

## 🚀 Features

* User registration
* User authentication
* Task management
* RESTful API endpoints
* PostgreSQL database integration
* SQLAlchemy ORM
* Pydantic data validation
* Password hashing
* JWT-based authentication
* Modular project structure
* Interactive API documentation with Swagger UI

## 🛠️ Tech Stack

* **Python**
* **FastAPI**
* **SQLAlchemy**
* **PostgreSQL**
* **Pydantic**
* **JWT**
* **Argon2**
* **Uvicorn**
* **Alembic**

## 📁 Project Structure

```text
task_management/
│
├── src/
│   │
│   ├── tasks/
│   │   ├── __init__.py
│   │   ├── controller.py
│   │   ├── dtos.py
│   │   ├── models.py
│   │   └── router.py
│   │
│   ├── user/
│   │   ├── __init__.py
│   │   ├── controller.py
│   │   ├── dtos.py
│   │   ├── models.py
│   │   └── router.py
│   │
│   └── utils/
│       ├── __init__.py
│       ├── constant.py
│       ├── db.py
│       ├── helper.py
│       └── settings.py
│
├── main.py
├── .gitignore
├── requirements.txt
└── README.md
```

## 📌 Architecture

The project separates responsibilities into different layers.

### User Module

The `user` module handles user-related functionality.

```text
user/
├── controller.py
├── dtos.py
├── models.py
└── router.py
```

* `models.py` → Database models
* `dtos.py` → Request/response schemas
* `controller.py` → Business logic
* `router.py` → API endpoints

### Task Module

The `tasks` module handles task-related functionality.

```text
tasks/
├── controller.py
├── dtos.py
├── models.py
└── router.py
```

### Utils Module

The `utils` module contains common application functionality.

```text
utils/
├── constant.py
├── db.py
├── helper.py
└── settings.py
```

* `db.py` → Database connection and configuration
* `settings.py` → Application settings
* `constant.py` → Application constants
* `helper.py` → Common helper functions

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/<your-repository>.git
cd task_management
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

## 🔐 Environment Variables

Create a `.env` file in the project root.

Example:

```env
DB_CON=postgresql://username:password@localhost:5432/task_management
SECRET_KEY=your_secret_key
ALGORITHM=HS256
EXP_TIME=30
```

**Do not upload `.env` to GitHub.**

Make sure `.env` is included in `.gitignore`.

## 🗄️ Database

This project uses **PostgreSQL** as the database and **SQLAlchemy** as the ORM.

Create a PostgreSQL database:

```text
task_management
```

Then configure the database connection in your `.env` file.

Example:

```env
DB_CON=postgresql://postgres:password@localhost:5432/task_management
```

## ▶️ Running the Application

Start the FastAPI development server:

```bash
uvicorn main:app --reload
```

The application will run at:

```text
http://127.0.0.1:8000
```

## 📖 API Documentation

FastAPI automatically generates interactive API documentation.

### Swagger UI

```text
http://127.0.0.1:8000/docs
```

### ReDoc

```text
http://127.0.0.1:8000/redoc
```

You can use Swagger UI to test the API endpoints directly from your browser.

## 👤 User Registration

Example registration request:

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

These credentials are only examples for testing.

## 🔑 Authentication

The application uses authentication mechanisms to protect user-specific resources.

Passwords should be stored using secure hashing rather than plain text.

JWT tokens can be used to authenticate requests after successful login.

## 📝 Task Management

The task module is responsible for managing tasks associated with users.

Typical task operations can include:

* Create a task
* View tasks
* Update a task
* Delete a task
* Manage task status
* Associate tasks with users

## 🧪 Development

Run the application in development mode:

```bash
uvicorn main:app --reload
```

The `--reload` option automatically reloads the server whenever source files are modified.

## 🔮 Future Improvements

* [ ] Complete CRUD operations for tasks
* [ ] Add task priorities
* [ ] Add task deadlines
* [ ] Add task status tracking
* [ ] Add user-specific authorization
* [ ] Add refresh tokens
* [ ] Add pagination
* [ ] Add search and filtering
* [ ] Add automated tests
* [ ] Add Docker support
* [ ] Add CI/CD using GitHub Actions
* [ ] Deploy the API to the cloud

## 👨‍💻 Author

**Atul Mall**

Computer Science & Engineering Student

## 📄 License

This project is created for learning and development purposes.
