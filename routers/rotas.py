from fastapi import APIRouter
from controllers.user_controller import get_all_users


router = APIRouter()

@router.get("/users")
def list_users():
    return get_all_users()
