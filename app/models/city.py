from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from app.core.db import Base


class Cities(Base):
    name = Column(String(100))
    weathers = relationship("OpenWeather", back_populates="city")
    openweather_id = Column(Integer)
