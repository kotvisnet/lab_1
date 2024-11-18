from Animal import Animal

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, "Кошка")
        self.color = color

    def __str__(self):
        return f"{self.name} - {self.color} (Кошка)"