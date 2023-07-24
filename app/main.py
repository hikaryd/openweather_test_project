from apscheduler.schedulers.asyncio import AsyncIOScheduler
from fastapi import FastAPI

from app.api.routers import main_router
from app.core.config import settings
from app.services import get_weather

app = FastAPI(title=settings.app_title)

app.include_router(main_router)


@app.on_event("startup")
async def startup():
    scheduler = AsyncIOScheduler()
    scheduler.add_job(get_weather, "cron", hour="*/1")
    scheduler.start()
