from fastapi import APIRouter

from Users.schemas import CreateUser
from Users import crud


router = APIRouter(prefix='/users', tags=['users'])

@router.post('/')
def create_user(user: CreateUser):
    return crud.create_user(user_in=user)