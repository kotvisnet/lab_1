from Animal import Animal
from AnimalJSONHander import AnimalJSONHandler
from AnimalXMLHandler import AnimalXMLHandler

animal = Animal('Denis', 'Cat')
print(f"animal:\t{animal}")

animalJSON = AnimalJSONHandler("C:\\Users\eldor\PycharmProjects\lab1\JSON")

animalJSON.create(animal)

example = animalJSON.read('Denis')

print(example)

animal = Animal('Leva', 'Dog')
print(f"animal:\t{animal}")

animalXML = AnimalJSONHandler("C:\\Users\eldor\PycharmProjects\lab1\XML")

animalXML.create(animal)

example = animalXML.read('Leva')
































# # Попытка усыновить снова
# try:
#     shelter.adopt_animal(dog)  # Это вызовет ошибку, потому что собака уже усыновлена
# except ValueError as e:
#     print(e)
#
# # Возврат животного в приют
# dog.return_to_shelter()
# shelter.return_animal(dog)
#
# # Пробуем добавить неподобающий объект в приют
# try:
#     shelter.add_animal("Строка вместо животного")  # Это вызовет ошибку
# except AssertionError as e:
#     print("Ошибка:", e)
#
# # Пример с исключением для полного приюта
# try:
#     full_shelter = Shelter("Переполненный приют")
#     for _ in range(101):  # Допустим, приют может вмещать только 100 животных
#         full_shelter.add_animal(Dog("Собака №" + str(_), "Беспородная"))
#     full_shelter.add_animal(Dog("Новая собака", "Мопс"))
# except ShelterFullError as e:
#     print("Ошибка:", e)
