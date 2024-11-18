from Animal import Animal

class Bird(Animal):
    def __init__(self, name, wing_span):
        super().__init__(name, "Птица")
        self.wing_span = wing_span

    def __str__(self):
        return f"{self.name} с размахом крыльев {self.wing_span} см (Птица)"