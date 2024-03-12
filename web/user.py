from fastapi import APIRouter
router = APIRouter(prefix = "/user")


@router.get("/")
def get_user():
    return {"message": "Welcome"}