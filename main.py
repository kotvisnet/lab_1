from Animal import Animal
from Dog import Dog
from Cat import Cat
from Shelter import Shelter
from Bird import Bird
from AdoptionProcess import  AdoptionProcess
from Veterinarian import  Veterinarian
from AnimalJSONHander import AnimalJSONHandler

# Пример использования

# # Создание животных
# dog = Dog("Бобик", "Овчарка")
# dogTwo = Dog("Лева", "Дворняга")
# cat = Cat("Мурка", "Черная")
# bird = Bird("Кеша", 25)
#
# # Создание приюта
# shelter = Shelter("Приют для животных")
#
# # Добавление животных в приют
# shelter.add_animal(dog)
# shelter.add_animal(dogTwo)
# shelter.add_animal(cat)
# shelter.add_animal(bird)
#
# # Просмотр всех животных в приюте
# print("Все животные в приюте:")
# shelter.list_animals()
#
# # Процесс усыновления
# adoption_process = AdoptionProcess()
# adoption_process.start_adoption(dog, "Иван")
# adoption_process.approve_adoption(dog)
#
# # Ветеринар проверяет здоровье
# vet = Veterinarian("Д-р Петров")
# vet.check_health(dog)

animal = Animal('Denis', 'Cat')
print(f"animal:\t{animal}")

animalJSON = AnimalJSONHandler("C:\\Users\eldor\PycharmProjects\lab1\JSON")

animalJSON.create(animal)

example = animalJSON.read('Denis')

print(example)
































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
