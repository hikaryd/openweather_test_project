from typing import List

from fastapi import Depends
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.crud import openweather_crud
from app.schemas import WeatherDB

router = InferringRouter()


@cbv(router)
class WeatherCBV:
    session: AsyncSession = Depends(get_async_session)

    @router.get(
        "/last_hour",
    )
    async def get_last_hour(self) -> List[WeatherDB]:
        weather_last_hour = await openweather_crud.get_multi_last_hour(
            session=self.session
        )
        return weather_last_hour

    @router.get(
        "/",
    )
    async def get_all(self) -> List[WeatherDB]:
        weather_all = await openweather_crud.get_multi(session=self.session)
        return weather_all

    @router.get(
        "/{city_name}",
    )
    async def get_weather_in_city(self, city_name: str) -> List[WeatherDB]:
        weather_all = await openweather_crud.get_by_attribute(
            attr_name="name",
            attr_value=city_name,
            session=self.session,
        )
        return weather_all

    @router.get(
        "/last_hour/{city_name}",
    )
    async def get_weather_in_city_last_hour(self, city_name: str) -> List[WeatherDB]:
        weather_last_hour = await openweather_crud.get_by_attribute_last_hour(
            attr_name="name",
            attr_value=city_name,
            session=self.session,
        )
        return weather_last_hour
