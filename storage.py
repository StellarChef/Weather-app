from models import City
import json


class Storage:
    FILE_NAME = "storage.json"

    def _load_from_storage(self) -> list[dict]:
        try:
            with open(self.FILE_NAME, "r") as file:
                data = json.load(file)
                return data["cities"]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def _save_storage(self, storage: list[dict]):
        with open(self.FILE_NAME, "w") as file:
            json.dump({"cities": storage}, file, indent=2)

    def add_to_storage(self, item: City):
        storage = self._load_from_storage()

        storage.append(item.model_dump(mode="json"))

        self._save_storage(storage)

    def get_all(self) -> list[City]:
        data = self._load_from_storage()
        return [City.model_validate(x) for x in data]
