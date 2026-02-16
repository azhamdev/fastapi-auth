# FastAPI Auth Boilerplate

Boilerplate untuk belajar Authentication dan Authorization menggunakan FastAPI.

## Teknologi

- **FastAPI** - Web framework
- **SQLModel** - ORM
- **SQLite** - Database
- **Alembic** - Database migrations
- **Pydantic** - Data validation
- **JWT** - Authentication (via python-jose)
- **bcrypt** - Password hashing
- **Scalar** - API Documentation

## Struktur Project

```
fastapi-auth/
├── app/
│   ├── __init__.py
│   ├── main.py                 # Entry point aplikasi
│   ├── models/
│   │   └── engine.py           # Database engine configuration
│   └── modules/
│       ├── __init__.py
│       ├── auth/               # Module Authentication
│       │   ├── __init__.py
│       │   ├── router.py       # Auth endpoints (register, login)
│       │   ├── schema.py       # Auth Pydantic schemas
│       │   └── utils.py        # Auth helper functions
│       └── post/               # Module Posts (contoh protected routes)
│           ├── __init__.py
│           └── router.py       # Post endpoints
├── alembic/                    # Database migrations
├── pyproject.toml              # Project dependencies
├── Makefile                    # Useful commands
└── database.db                 # SQLite database
```

## Quick Start

### 1. Install Dependencies

```bash
uv sync
```

### 2. Jalankan Development Server

```bash
make dev
```

atau

```bash
uv run uvicorn app.main:app --reload --port 8000
```

### 3. Akses API Documentation

- Swagger UI: http://localhost:8000/docs
- Scalar: http://localhost:8000/scalar
- Redoc: http://localhost:8000/redoc

## Endpoint API

### Auth Routes

| Method | Endpoint       | Description         |
|--------|----------------|---------------------|
| POST   | /auth/register | Register user baru  |
| POST   | /auth/login    | Login user          |

### Post Routes (Contoh Protected Routes)

| Method | Endpoint | Description        |
|--------|----------|--------------------|
| GET    | /posts/  | Get semua posts    |

## Learning Objectives

Dengan boilerplate ini, student akan belajar:

1. **Authentication**
   - Password hashing dengan bcrypt
   - JWT token generation dan validation
   - User registration dan login

2. **Authorization**
   - Protected routes dengan JWT dependency
   - Role-based access control (RBAC)
   - Current user injection

3. **Database**
   - SQLModel models
   - Database migrations dengan Alembic
   - CRUD operations

4. **API Best Practices**
   - Pydantic schemas untuk validation
   - Modular router structure
   - Error handling

## Environment Variables

Buat file `.env` di root project:

```env
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

## Commands

```bash
# Development server
make dev

# Database migrations
alembic revision --autogenerate -m "message"
alembic upgrade head

# Run with uvicorn directly
uv run uvicorn app.main:app --reload --port 8000
```

## Devscale Indonesia

Boilerplate ini dibuat untuk student [Devscale Indonesia](https://devscale.id) dalam mempelajari Authentication dan Authorization pada backend development.

---

Selamat belajar! Jangan ragu untuk modify dan experiment dengan boilerplate ini.
