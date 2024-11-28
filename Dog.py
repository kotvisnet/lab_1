from Animal import Animal

class Dog(Animal):
    def __init__(self, name: str, breed: str):
        super().__init__(name, "Собака")
        self.breed = breed

    def __str__(self):
        return f"{self.name} - {self.breed} (Собака)"
