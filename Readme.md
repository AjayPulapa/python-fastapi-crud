FastAPI + MySQL CRUD Application

A simple, modular, production-ready CRUD application using FastAPI, SQLAlchemy, and MySQL.
This project follows a clean architecture with config, controller, model, schema, and service layers.

🚀 Features

FastAPI with automatic Swagger UI

MySQL database connection

SQLAlchemy ORM

CRUD operations (Create, Read, Update, Delete)

Modular & scalable folder structure

Pydantic v2 schemas

📁 Folder Structure
python-crud/
│
├── app/
│   ├── main.py
│   │
│   ├── config/
│   │   └── database.py
│   │
│   ├── controller/
│   │   └── user_controller.py
│   │
│   ├── models/
│   │   └── user.py
│   │
│   ├── schemas/
│   │   └── user_schema.py
│   │
│   ├── service/
│   │   └── user_service.py
│
├── .env
├── requirements.txt
├── venv/
└── __pycache__/

🛠 1. Create Virtual Environment
Windows
python -m venv venv

macOS / Linux
python3 -m venv venv

🔄 2. Activate Virtual Environment
Windows (CMD)
venv\Scripts\activate

Windows (PowerShell)
.\venv\Scripts\Activate.ps1

macOS / Linux
source venv/bin/activate

📦 3. Install Dependencies

Create a requirements.txt and add:

fastapi
uvicorn
sqlalchemy
pymysql
python-dotenv


Then install:

pip install -r requirements.txt

🗄 4. Create .env File

Create a .env file in the project root:

DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=yourpassword
DB_NAME=fastapi_crud


Make sure your MySQL server is running.

🗃 5. Create MySQL Database

Run this in MySQL:

CREATE DATABASE fastapi_crud;

▶️ 6. Run the FastAPI Application

Run the server from the project root:

uvicorn app.main:app --reload


If inside python-crud/ folder, use:

uvicorn app.main:app --reload

🌐 7. Open API Docs

FastAPI automatically generates Swagger UI:

🚀 Swagger UI:

http://127.0.0.1:8000/docs


📄 Alternative Redoc UI:

http://127.0.0.1:8000/redoc

🧪 8. Test API Endpoints
📌 Create User (POST /users/)
{
  "name": "Ajay",
  "email": "ajay@example.com"
}

📌 Get All Users (GET /users/)
📌 Get User By ID (GET /users/{id})
📌 Update User (PUT /users/{id})
📌 Delete User (DELETE /users/{id})