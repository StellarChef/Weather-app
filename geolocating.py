import requests
from pydantic import BaseModel
import json


class Cords(BaseModel):
    latitude: float
    longitude: float


class Weather:
    def __init__(self, city_name: str):
        self.city = city_name
        self.coords = self._geolocate(city_name)
        self.temperature = self._fetch_weather()

    def _geolocate(self, city_name: str) -> dict:
        resp = requests.get(
            "https://geocoding-api.open-meteo.com/v1/search",
            params={"name": city_name, "format": "json"},
        )
        data = resp.json()
        lat = data["results"][0]["latitude"]
        lon = data["results"][0]["longitude"]
        return {"latitude": lat, "longitude": lon}

    def _fetch_weather(self):
        resp = requests.get(
            "https://api.open-meteo.com/v1/forecast",
            params={
                "latitude": self.coords["latitude"],
                "longitude": self.coords["longitude"],
                "current": "temperature_2m",
            },
        )

        data = resp.json()
        temperature = data["current"]["temperature_2m"]
        return temperature

    def show(self):
        print(self.city)
        print(self.coords)
        print(self.temperature)


Berlin = Weather("Berlin")
Berlin.show()
