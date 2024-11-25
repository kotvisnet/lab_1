import json
from typing import Optional
from Animal import Animal


class AnimalExistsError(Exception):
    pass
class AnimalNotFoundError(Exception):
    pass

class AnimalJSONHandler:
    def __init__(self, filepath: str):
        self.filepath = filepath

    def create(self, animal: Animal):
        animal_data = {
            "name": animal.name,
            "species": animal.species,
            "adopted": animal.adopted
        }
        try:
            with open(self.filepath, "r") as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = {"animals": []}

        for existing_animals in data.get("animals", []):
            if existing_animals["name"] == animal.name:
                raise AnimalExistsError(f"Animal '{animal.name}' already exists.")

        data["animals"].append(animal_data)
        with open(self.filepath, "w") as file:
            json.dump(data, file, indent=4)

    def read(self, name: str) -> Optional[Animal]:
        try:
            with open(self.filepath, "r") as file:
                data = json.load(file)
            for animal_data in data.get("animals", []):
                if animal_data["name"] == name:
                    return Animal(animal_data['name'], animal_data['species'], animal_data['adopted'])
        except (FileNotFoundError, json.JSONDecodeError):
            return None

    def update(self, name: str, new_name: str):
        try:
            with open(self.filepath, "r") as file:
                data = json.load(file)
            for animal_data in data.get("animals", []):
                if animal_data["name"] == name:
                    animal_data["name"] = new_name
                    with open(self.filepath, "w") as file:
                        json.dump(data, file, indent=4)
                    return True
            raise AnimalNotFoundError(f"Author '{name}' not found for update.")
        except (FileNotFoundError, json.JSONDecodeError):
            return False
        except AnimalNotFoundError as e:
            print(e)
            return False

    def delete(self, name: str):
        try:
            with open(self.filepath, "r") as file:
                data = json.load(file)
            original_length = len(data.get("animals", []))
            data["animals"] = [animals for animals in data.get("animals", []) if animals["name"] != name]

            if len(data["animals"]) == original_length:
                raise AnimalNotFoundError(f"Animal '{name}' not found for deletion.")

            with open(self.filepath, "w") as file:
                json.dump(data, file, indent=4)
            return True
        except (FileNotFoundError, json.JSONDecodeError):
            return False
        except AnimalNotFoundError as e:
            print(e)
            return False