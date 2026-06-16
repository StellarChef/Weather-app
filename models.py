from pydantic import BaseModel


class City(BaseModel):
    name: str
    coords: dict
    temperature: float | None = 0
    condition: float | None = 0
