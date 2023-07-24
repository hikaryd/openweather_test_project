import time

from sqlalchemy import Column, Float, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.core.db import Base


class OpenWeather(Base):
    city_id = Column(Integer, ForeignKey("cities.id"))
    city = relationship("Cities", back_populates="weathers")
    wind_speed = Column(Float)
    temp = Column(Float)
    temp_max = Column(Float)
    temp_min = Column(Float)
    create_time = Column(Float, default=time.time)
