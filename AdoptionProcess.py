from Animal import Animal

from typing import Optional
class AdoptionProcess:
    def __init__(self):
        self.pending_adoptions = []

    def start_adoption(self, animal: Optional[Animal], adopter: str):
        assert isinstance(animal, Animal), "Объект должен быть экземпляром класса Animal."
        assert isinstance(adopter, str), "Имя усыновителя должно быть строкой."
        print(f"Процесс усыновления для {animal.name} начат. Усыновитель: {adopter}.")
        self.pending_adoptions.append((animal, adopter))

    def approve_adoption(self, animal):
        for i, (a, _) in enumerate(self.pending_adoptions):
            if a == animal:
                print(f"Усыновление {animal.name} одобрено!")
                self.pending_adoptions.pop(i)
                return
        raise ValueError(f"Процесс усыновления для {animal.name} не был начат.")

    def reject_adoption(self, animal):
        for i, (a, _) in enumerate(self.pending_adoptions):
            if a == animal:
                print(f"Усыновление {animal.name} отклонено.")
                self.pending_adoptions.pop(i)
                return
        raise ValueError(f"Процесс усыновления для {animal.name} не был начат.")
