from fastapi import APIRouter
from api.routes import sample,console

api_router=APIRouter()


api_router.include_router(console.router,prefix="/console",tags=["console"])
api_router.include_router(sample.router,prefix="/sample",tags=["sample"])