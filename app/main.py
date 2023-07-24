from apscheduler.schedulers.asyncio import AsyncIOScheduler
from fastapi import FastAPI

from app.api.routers import main_router
from app.core.config import settings
from app.core.db import AsyncSessionLocal
from app.crud import cities_crud
from app.services import get_weather, get_city_by_name

app = FastAPI(title=settings.app_title)

app.include_router(main_router)


@app.on_event("startup")
async def startup():
    scheduler = AsyncIOScheduler()
    scheduler.add_job(get_weather, "cron", hour="*/1")
    scheduler.start()

    # Данный кусок кода нужен просто для добавление 50 крупнейших городов мира
    for city in settings.CITIES:
        city_data = await get_city_by_name(city)
        if city_data is None:
            continue
        async with AsyncSessionLocal() as session:
            city = await cities_crud.get_by_attribute(
                attr_name="name",
                attr_value=city_data.name,
                session=session,
            )
            if city:
                continue
            await cities_crud.create(obj_in=city_data, session=session)
