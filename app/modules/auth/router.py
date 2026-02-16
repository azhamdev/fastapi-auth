from fastapi import APIRouter

auth_router = APIRouter(prefix="/auth", tags=["Auth"])


@auth_router.post("/register")
def register_user():
    return {}


@auth_router.post("/login")
def login_user():
    return {}
