from typing import Optional
from Animal import Animal

class Veterinarian:
    def __init__(self, name):
        self.name = name

    def check_health(self, animal: Optional[Animal]):
        assert isinstance(animal, Animal), "Переданный объект должен быть экземпляром класса Animal."
        print(f"Ветеринар {self.name} проверил здоровье {animal.name}. Здоровье в норме.")

    def perform_surgery(self, animal):
        assert isinstance(animal, Animal), "Переданный объект должен быть экземпляром класса Animal."
        print(f"Ветеринар {self.name} провел операцию {animal.name}.")
