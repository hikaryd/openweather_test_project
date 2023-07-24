from typing import Union

import httpx

from app.core.config import settings
from app.schemas import CityCreate


async def get_city_by_name(city_name: str) -> Union[CityCreate, None]:
    async with httpx.AsyncClient() as client:
        res = await client.get(
            "http://api.openweathermap.org/data/2.5/find",
            params={
                "q": city_name,
                "type": "like",
                "units": "metric",
                "lang": "ru",
                "APPID": settings.openweathermap_key,
            },
        )
        data = res.json()
        if "list" in data and data["list"]:
            return CityCreate(
                openweather_id=data["list"][0]["id"],
                name=data["list"][0]["name"],
            )
        return None
