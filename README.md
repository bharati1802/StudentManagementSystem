# 🎓 Student Information Management System

A professional Full-Stack web application designed to manage student records efficiently. This project utilizes **FastAPI** for a high-performance backend and **Streamlit** for an intuitive, interactive user interface.

## 🚀 Overview
This system allows users to create, read, and manage student data (Roll Number, Name, and Standard) in a persistent **MySQL** database. It demonstrates the implementation of a decoupled architecture where the frontend and backend communicate via **RESTful APIs**.

## 🛠️ Tech Stack
- **Frontend:** Streamlit (Python-based UI framework)
- **Backend:** FastAPI (Modern, fast web framework)
- **Database:** MySQL
- **ORM:** SQLAlchemy (Object Relational Mapping)
- **Driver:** PyMySQL & Cryptography (for secure database connection)
- **Communication:** REST API (JSON)

## 📁 Project Structure
- `StudentInfo.py`: The Backend core containing API endpoints and database models.
- `app_ui.py`: The Frontend application providing the user interface.
- `README.md`: Project documentation and setup guide.

## ⚙️ Setup & Installation

### 1. Prerequisites
Ensure you have a MySQL server running and a database named `cric_db_mysql` (or update the URL in the code).

### 2. Virtual Environment
Create and activate a virtual environment to keep dependencies isolated:
```bash
python -m venv .venv
# On Windows:
.venv\Scripts\activate
