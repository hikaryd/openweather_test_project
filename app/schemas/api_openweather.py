from typing import List, Optional

from pydantic import BaseModel


class Coord(BaseModel):
    lon: float
    lat: float


class WeatherItem(BaseModel):
    id: int
    main: str
    description: str
    icon: str


class Main(BaseModel):
    temp: float
    feels_like: float
    temp_min: float
    temp_max: float
    pressure: int
    humidity: int
    sea_level: int
    grnd_level: int


class Wind(BaseModel):
    speed: float
    deg: int
    gust: Optional[float]


class Clouds(BaseModel):
    all: int


class Sys(BaseModel):
    type: Optional[int]
    id: int
    country: str
    sunrise: int
    sunset: int


class OpenWeatherCity(BaseModel):
    pass


class ApiOpenWeather(BaseModel):
    coord: Coord
    weather: Optional[List[WeatherItem]]
    base: str
    main: Main
    visibility: Optional[int]
    wind: Wind
    clouds: Clouds
    dt: int
    sys: Sys
    timezone: int
    id: int
    name: str
    cod: int
