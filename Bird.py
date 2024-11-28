from Animal import Animal

class Bird(Animal):
    def __init__(self, name: str, wing_span: str):
        super().__init__(name, "Птица")
        self.wing_span = wing_span

    def __str__(self):
        return f"{self.name} с размахом крыльев {self.wing_span} см (Птица)"
