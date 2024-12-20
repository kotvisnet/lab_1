from Animal import Animal
from typing import Optional

class Shelter:
    def __init__(self, name: str):
        self.name = name
        self.animals = []

    def add_animal(self, animal: Optional[Animal]):
        assert isinstance(animal, Animal), "Можно добавить только экземпляры класса Animal или его подкласы."
        self.animals.append(animal)

    def adopt_animal(self, animal: Optional[Animal]):
        if animal not in self.animals:
            raise ValueError(f"{animal.name} не найден в приюте.")
        animal.adopt()
        self.animals.remove(animal)

    def return_animal(self, animal: Optional[Animal]):
        if animal in self.animals:
            raise ValueError(f"{animal.name} уже в приюте.")
        self.animals.append(animal)
        animal.return_to_shelter()

    def list_animals(self):
        if not self.animals:
            print("Приют пуст!")
        else:
            for animal in self.animals:
                print(animal)