import xml.etree.ElementTree as ET
from typing import Optional

from Animal import Animal


class AnimalExistsError(Exception):
    pass

class AnimalNotFoundError(Exception):
    pass

class AnimalXMLHandler:
    def __init__(self, filepath: str):
        self.filepath = filepath

    def create(self, animal: Animal):
        try:
            tree = ET.parse(self.filepath)
            root = tree.getroot()
        except (FileNotFoundError, ET.ParseError):
            root = ET.Element("animals")

        for animal_element in root.findall("animal"):
            if animal_element.find("name").text == animal.name:
                raise AnimalExistsError(f"Animal '{animal.name}' already exists.")
        animal_element = ET.SubElement(root, "animal")
        ET.SubElement(animal_element, "name").text = animal.name
        ET.SubElement(animal_element, "species").text = animal.species
        ET.SubElement(animal_element, "adopted").text = str(animal.adopted)
        tree = ET.ElementTree(root)
        tree.write(self.filepath)

    def read(self, name: str) -> Optional[Animal]:
        try:
            tree = ET.parse(self.filepath)
            root = tree.getroot()

            for animal_element in root.findall("animal"):
                if animal_element.find("name").text == name:
                    species = animal_element.find("species").text
                    adopted = bool(animal_element.find("adopted").text)
                    return Animal(name, species, adopted)
        except (FileNotFoundError, ET.ParseError):
            return None
        return None

    def update(self, name: str, new_species: str) -> bool:
        try:
            tree = ET.parse(self.filepath)
            root = tree.getroot()
            for animal_element in root.findall("animal"):
                if animal_element.find("name").text == name:
                    animal_element.find("species").text = new_species
                    tree.write(self.filepath)
                    return True

            raise AnimalNotFoundError(f"Animal '{name}' not found for update.")
        except (FileNotFoundError, ET.ParseError):
            return False
        except AnimalNotFoundError as e:
            print(e)
            return False

    def delete(self, name: str) -> bool:
        try:
            tree = ET.parse(self.filepath)
            root = tree.getroot()
            for animal_element in root.findall("animal"):
                if animal_element.find("name").text == name:
                    root.remove(animal_element)
                    tree.write(self.filepath)
                    return True

            raise AnimalNotFoundError(f"Animal '{name}' not found for deletion.")
        except (FileNotFoundError, ET.ParseError):
            return False
        except AnimalNotFoundError as e:
            print(e)
            return False

