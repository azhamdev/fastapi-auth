from fastapi import APIRouter

post_router = APIRouter(prefix="/posts", tags=["Posts"])


@post_router.get("/")
def get_posts():
    return {"posts": []}
