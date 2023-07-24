from pydantic import BaseModel


class CityDB(BaseModel):
    id: int
    name: str
    openweather_id: int

    class Config:
        orm_mode = True


class CityCreate(BaseModel):
    name: str
    openweather_id: int
