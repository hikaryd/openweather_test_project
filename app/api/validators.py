from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud import cities_crud


async def city_exists(
    city_id: int,
    session: AsyncSession,
) -> None:
    city = await cities_crud.get(city_id, session)
    if city is None:
        raise HTTPException(status_code=404, detail="Город не найден!")


async def city_name_already_exists(
    city_name: int,
    session: AsyncSession,
) -> None:
    city = await cities_crud.get_by_attribute(
        attr_name="name",
        attr_value=city_name,
        session=session,
    )
    if city is not None:
        raise HTTPException(status_code=404, detail="Такой город уже существует.")
