from pydantic import BaseModel

from app.schemas.city import CityDB


class WeatherDB(BaseModel):
    city: CityDB
    wind_speed: float
    temp: float
    temp_max: float
    temp_min: float
    create_time: int

    class Config:
        orm_mode = True


class WeatherCreate(BaseModel):
    city_id: int
    wind_speed: float
    temp: float
    temp_max: float
    temp_min: float
