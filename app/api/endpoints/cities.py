import logging
from typing import List

from fastapi import Depends, HTTPException
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from sqlalchemy.ext.asyncio import AsyncSession

from app.api import validators
from app.core.db import get_async_session
from app.crud import cities_crud
from app.schemas import CityCreate, CityDB
from app.services import get_city_by_name

router = InferringRouter()


@cbv(router)
class CitiesCBV:
    session: AsyncSession = Depends(get_async_session)

    @router.get(
        "/",
    )
    async def get_all(self) -> List[CityDB]:
        all_cities = await cities_crud.get_multi(session=self.session)
        return all_cities

    @router.post(
        "/{city_name}",
    )
    async def create(
        self,
        city_name: str,
    ) -> CityDB:
        city = await get_city_by_name(city_name)
        if city is None:
            raise HTTPException(
                status_code=404,
                detail="Город с таким названием не найден",
            )
        city = await cities_crud.create(obj_in=city, session=self.session)
        return city

    @router.delete(
        "/{city_id}",
    )
    async def delete(self, city_id: int) -> CityDB:
        await validators.city_exists(city_id, session=self.session)
        charity = await cities_crud.delete(model_id=city_id, session=self.session)
        return charity
