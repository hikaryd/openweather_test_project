from fastapi import APIRouter

from app.api.endpoints import openweather_router, cities_router

main_router = APIRouter()
main_router.include_router(
    openweather_router,
    prefix="/weather",
    tags=["Weather"],
)
main_router.include_router(
    cities_router,
    prefix="/city",
    tags=["Cities"],
)
