from fastapi import APIRouter, HTTPException, Depends

from api.users.model import User
from service.auth.index import get_current_active_user

router = APIRouter()

@router.get("/")
async def read():
    users = await User.find().to_list()
    return users

@router.get("/{user_id}", response_model=User, dependencies=[Depends(get_current_active_user)])
async def read_single(id: str):
    user = await User.get(id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.post("/")
async def create(user: User):
    await user.create()
    return user

