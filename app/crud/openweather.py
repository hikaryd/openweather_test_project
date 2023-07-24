import time

import sqlalchemy as sq
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from app.crud.base import CRUDBase, ModelType
from app.models import OpenWeather


class OpenWeatherCRUD(CRUDBase[OpenWeather]):
    async def get_multi_last_hour(self, session: AsyncSession):
        last_hour = int(time.time()) - 3600
        db_objs = await session.execute(
            sq.select(self.model)
            .where(self.model.create_time >= last_hour)
            .options(joinedload(OpenWeather.city))
        )
        return db_objs.scalars().all()

    async def get_multi(self, session: AsyncSession):
        db_objs = await session.execute(
            sq.select(self.model).options(joinedload(OpenWeather.city))
        )
        return db_objs.scalars().all()

    async def get_by_attribute_last_hour(
        self,
        attr_name: str,
        attr_value: str,
        session: AsyncSession,
    ) -> ModelType:
        attr = getattr(self.model, attr_name)
        db_obj = await session.execute(sq.select(self.model).where(attr == attr_value))
        return db_obj.scalars().first()


openweather_crud = OpenWeatherCRUD(OpenWeather)
