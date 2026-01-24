# 🚀 Productivity Platform – FastAPI Backend

A production-ready backend API built with **FastAPI** for managing tasks and productivity workflows.  
This project demonstrates real-world backend development practices: clean architecture, full CRUD, validations, environment-based configuration, and live deployment.

🔗 **Live API:**  
https://productivity-platform.onrender.com  
📘 **Swagger Docs:**  
https://productivity-platform.onrender.com/docs

---

## 🧠 Project Overview

This backend service provides a RESTful API to manage tasks, designed with scalability and maintainability in mind.  
It follows modern backend standards and is ready to be consumed by any frontend application.

Key goals of this project:
- Demonstrate professional FastAPI usage
- Apply clean architecture and best practices
- Deploy a live backend service to the cloud

---

## ✨ Features

- Full **CRUD operations** for tasks
- **FastAPI** with automatic Swagger documentation
- **SQLAlchemy ORM**
- **Pydantic** schemas with validations
- **Timestamps** (`created_at`, `updated_at`)
- Environment-based configuration using `.env`
- **CORS enabled** (frontend-ready)
- Deployed and publicly accessible

---

## 🛠️ Tech Stack

- **Python 3**
- **FastAPI**
- **SQLAlchemy**
- **Pydantic / Pydantic Settings**
- **SQLite**
- **Uvicorn**
- **Render (deployment)**

---

## 📂 Project Structure

```text
backend/
├── app/
│   ├── core/        # Config, database, dependencies

│   ├── models/      # SQLAlchemy models

│   ├── routers/     # API routes

│   ├── schemas/     # Pydantic schemas

│   └── main.py      # Application entry point

├── requirements.txt

└── .env (ignored)


---

## 📌 API Endpoints

| Method | Endpoint        | Description         |
|-------|-----------------|---------------------|
| POST  | `/tasks`        | Create a new task   |
| GET   | `/tasks`        | Retrieve all tasks  |
| GET   | `/tasks/{id}`   | Retrieve task by ID |
| PUT   | `/tasks/{id}`   | Update a task       |
| DELETE| `/tasks/{id}`   | Delete a task       |

All endpoints can be tested directly via Swagger UI.

---

## ⚙️ Environment Variables

Example `.env` file:

DATABASE_URL=sqlite:///./tasks.db
ENV=development


---

## 🚀 Running the Project Locally

git clone https://github.com/fofos123-CPU/productivity-platform.git

cd productivity-platform/backend

python -m pip install -r requirements.txt
uvicorn app.main:app --reload


Open:
- http://127.0.0.1:8000/docs

---

## 🌍 Deployment

This API is deployed on Render and is publicly accessible.

---

## 🎯 Purpose

This project is part of my professional portfolio as a **Systems & Information Technologies Engineer**, demonstrating backend API design, clean architecture, and real deployment experience.

---

## 👨‍💻 Author

**Rodolfo Domínguez**  
Systems & Information Technologies Engineer  
Backend-focused | Open to multi-language development  

GitHub: https://github.com/fofos123-CPU
