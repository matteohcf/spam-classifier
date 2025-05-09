from fastapi import APIRouter
from api.auth.index import router as auth_router
from api.users.index import router as users_router


router = APIRouter()

router.include_router(auth_router, prefix="/auth", tags=["auth"])
router.include_router(users_router, prefix="/users", tags=["users"])
