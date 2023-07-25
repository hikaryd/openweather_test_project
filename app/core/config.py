from pydantic import BaseSettings


class Settings(BaseSettings):
    app_title: str = "TestProjectOpenWeather"
    database_url: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/postgres"
    secret: str = "secret"
    openweathermap_key: str = ""

    CITIES = [
        "Tokyo",
        "Delhi",
        "Shanghai",
        "Sao Paulo",
        "Mumbai",
        "Cairo",
        "Dhaka",
        "Osaka",
        "New York City",
        "Karachi",
        "Buenos Aires",
        "Chongqing",
        "Istanbul",
        "Kolkata",
        "Manila",
        "Rio de Janeiro",
        "Tianjin",
        "Kinshasa",
        "Guangzhou",
        "Los Angeles",
        "Moscow",
        "Shenzhen",
        "Lahore",
        "Bangalore",
        "Jakarta",
        "Chennai",
        "Lima",
        "Bangkok",
        "Johannesburg",
        "Hyderabad",
        "Mexico City",
        "Wuhan",
        "Hangzhou",
        "Chengdu",
        "Ahmedabad",
        "Kuala Lumpur",
        "Hong Kong",
        "Pune",
        "Riyadh",
        "Beijing",
        "Bogota",
        "Alexandria",
        "Ankara",
        "London",
        "Ho Chi Minh City",
        "Baghdad",
        "Bangalore",
        "Tehran",
        "Santiago",
        "Toronto",
    ]

    class Config:
        env_file = ".env"


settings = Settings()
