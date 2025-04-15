# FastAPI CRUD with SQLite

A lightweight FastAPI application implementing full CRUD operations with SQLite. Ideal for learning or building quick prototypes.

---

## 🚀 Features

-FastAPI-based RESTful AP
-SQLite database integratio
-Pydantic models for data validatio
-Modular code structur
-Auto-generated interactive API docs (Swagger UI

---

## 📁 Project Structure

```
├── app.py               # Main FastAPI application
├── crud.py              # CRUD operation functions
├── db.py                # Database connection and setup
├── model.py             # Pydantic and SQLAlchemy models
├── requirements.txt     # Project dependencies
├── pyvenv.cfg           # Python virtual environment configuration
├── .gitignore           # Git ignore file
├── Scripts/             # Virtual environment scripts
│   ├── activate
│   ├── activate.bat
│   ├── Activate.ps1
│   ├── deactivate.bat
│   ├── fastapi.exe
│   ├── pip.exe
│   ├── pip3.12.exe
│   ├── pip3.exe
│   ├── python.exe
│   ├── pythonw.exe
│   └── uvicorn.exe
└── Include/
    └── site/
        └── python3.12/
            └── greenlet/
                └── greenlet.h
```


---

## 🛠️ Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Og-Akash/fastapi-crud-sqlite.git
   cd fastapi-crud-sqlite
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**

   - **Windows:**

     ```bash
     venv\Scripts\activate
     ```

   - **Unix or MacOS:**

     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Running the Application

Start the FastAPI server using Uvicorn:

```bash
uvicorn app:app --reload
```

- Access the interactive API docs at: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- Access the alternative ReDoc documentation at: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 🧪 API Endpoints

- **GET** `/items/` - Retrieve a list of items
- **GET** `/items/{id}` - Retrieve a specific item by ID
- **POST** `/items/` - Create a new item
- **PUT** `/items/{id}` - Update an existing item
- **DELETE** `/items/{id}` - Delete an item

---

## 📦 Dependencies

- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Pydantic](https://pydantic-docs.helpmanual.io/)
