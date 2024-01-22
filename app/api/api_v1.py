from fastapi import APIRouter

from app.api.endpoints import user, login

api_router = APIRouter()
api_router.include_router(login.router, prefix='/login', tags=['login'])
api_router.include_router(user.router, prefix='/user', tags=['user'])