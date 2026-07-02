# week1-api

A simple REST API built with FastAPI and SQLite. My first backend project — built while learning backend engineering fundamentals.

## What it does

A basic items API with full CRUD — create, read, and delete items. Data persists in a SQLite database.

## Tech stack

- **Python 3.13** — language
- **FastAPI** — web framework
- **SQLAlchemy** — ORM for database interactions
- **SQLite** — lightweight local database
- **uvicorn** — ASGI server that runs the app

## Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | /health | Health check |
| GET | /items | Get all items |
| GET | /items/{id} | Get one item by id |
| POST | /items | Create a new item |
| DELETE | /items/{id} | Delete an item |

## Run locally

```bash
# clone the repo
git clone https://github.com/afiapoks/week1-api.git
cd week1-api

# create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# install dependencies
pip install fastapi uvicorn sqlalchemy python-dotenv

# set up environment variables
cp .env.example .env

# run the server
uvicorn main:app --reload
```

API will be live at http://127.0.0.1:8000
Docs at http://127.0.0.1:8000/docs

## What I learned

- HTTP request/response cycle
- REST API design — resources, verbs, status codes
- FastAPI routing and Pydantic validation
- SQLAlchemy ORM — models, sessions, queries
- Environment variables and secret management
- Git workflow — committing and pushing to GitHub