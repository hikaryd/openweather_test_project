import httpx

from app.core.config import settings
from app.core.db import AsyncSessionLocal
from app.crud import cities_crud, openweather_crud
from app.schemas import ApiOpenWeather
from app.schemas.openweather import WeatherCreate


async def get_weather_in_city(openweather_id: int):
    async with httpx.AsyncClient() as client:
        res = await client.get(
            "http://api.openweathermap.org/data/2.5/weather",
            params={
                "id": openweather_id,
                "units": "metric",
                "lang": "ru",
                "APPID": settings.openweathermap_key,
            },
        )
        return res.json()


async def get_weather():
    async with AsyncSessionLocal() as session:
        cities = await cities_crud.get_multi(session)
        city_data = [(city.id, city.openweather_id) for city in cities]

        for city_id, openweather_id in city_data:
            data = await get_weather_in_city(openweather_id)
            data = ApiOpenWeather(**data)
            create_data = WeatherCreate(
                city_id=city_id,
                wind_speed=data.wind.speed,
                temp=data.main.temp,
                temp_max=data.main.temp_max,
                temp_min=data.main.temp_min,
            )
            await openweather_crud.create(create_data, session=session)
