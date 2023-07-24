import logging

import httpx

from app.core.config import settings
from app.core.db import AsyncSessionLocal
from app.crud import cities_crud, openweather_crud
from app.schemas import ApiOpenWeather, WeatherDB
from app.schemas.openweather import WeatherCreate


async def get_weather():
    async with AsyncSessionLocal() as session:
        async with httpx.AsyncClient() as client:
            cities = await cities_crud.get_multi(session)
            for city in cities:
                res = await client.get(
                    "http://api.openweathermap.org/data/2.5/weather",
                    params={
                        "id": city.openweather_id,
                        "units": "metric",
                        "lang": "ru",
                        "APPID": settings.openweathermap_key,
                    },
                )
                data = ApiOpenWeather(**res.json())
                create_data = WeatherCreate(
                    city_id=city.id,
                    wind_speed=data.wind.speed,
                    temp=data.main.temp,
                    temp_max=data.main.temp_max,
                    temp_min=data.main.temp_min,
                )
                logging.basicConfig(level=logging.INFO)
                logger = logging.getLogger(__name__)
                logger.info(create_data.dict())
                await openweather_crud.create(create_data, session=session)
