from storage import Storage
from geolocating import Service


class WheatherApp:
    def __init__(self):
        self.storage = Storage()
        self.service = Service()
        self.cities = []

    def load_cities(self) -> list:
        self.cities = self.storage.get_all()
        for city in self.cities:
            self.service.fetch_weather(city)

        return self.cities

    def add_city(self, name):
        city = self.service.create_city(name)
        self.service.fetch_weather(city)
        self.cities.append(city)
        self.storage.add_to_storage(city)

    def remove_city(self, index):
        self.storage.remove(index)
        self.cities.pop(index)

    def show(self):
        line = "=" * 42
        print(line)
        print(f"  🌤️  WEATHER APP — {len(self.cities)} city/cities")
        print(line)

        if not self.cities:
            print("  (no cities yet — add some via add_city)")
            print(line)
            return

        for index, city in enumerate(self.cities):
            lat = city.coords.get("latitude")
            lon = city.coords.get("longitude")
            print(f"{index}  📍 {city.name}")
            print(f"     coordinates : {lat}, {lon}")
            print(f"     temperature : {city.temperature} °C")
            print(f"     weather code: {city.condition}")
            print("-" * 42)
