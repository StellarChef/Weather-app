from models import City
from geolocating import Service
from storage import Storage

city = Service.create_city("Berlin")
Service.geolocate("Berlin")
