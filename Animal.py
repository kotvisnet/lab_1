class Animal:
    def __init__(self, name: str, species):
        self.name = name
        self.species = species
        self.adopted = False

    def adopt(self):
        if self.adopted:
            raise ValueError(f"{self.name} уже был принят в семью!")
        self.adopted = True
        print(f"{self.name} был принят в семью!")

    def return_to_shelter(self):
        if not self.adopted:
            raise ValueError(f"{self.name} не был принят в семью и не может вернуться в приют.")
        self.adopted = False
        print(f"{self.name} вернулся в приют.")

    def __str__(self):
        return f"{self.name} ({self.species})"