import requests
from pydantic import BaseModel
from models import City
import json


class Service:

    @staticmethod
    def geolocate(city_name: str) -> dict:
        resp = requests.get(
            "https://geocoding-api.open-meteo.com/v1/search",
            params={"name": city_name, "format": "json"},
        )
        data = resp.json()
        results = data.get("results")
        if not results:
            raise ValueError(f"City '{city_name}' not found")
        lat = results[0]["latitude"]
        lon = results[0]["longitude"]
        coords = {"latitude": lat, "longitude": lon}
        return coords

    @staticmethod
    def fetch_weather(city: City):
        resp = requests.get(
            "https://api.open-meteo.com/v1/forecast",
            params={
                "latitude": city.coords["latitude"],
                "longitude": city.coords["longitude"],
                "current": "temperature_2m,weather_code",
            },
        )
        data = resp.json()
        temperature = data["current"]["temperature_2m"]
        weather_code = data["current"]["weather_code"]
        city.temperature = temperature
        city.condition = weather_code

    @staticmethod
    def create_city(name: str) -> City:
        coords = Service.geolocate(name)
        return City(name=name, coords=coords)
