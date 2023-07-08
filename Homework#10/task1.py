# task1
''
"""
📌 Решить задачи, которые не успели решить на семинаре.
📌 Доработаем задачи 5-6. Создайте класс-фабрику.
○ Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
○ Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.
"""


class Animal:
    def __init__(self, name: object, age: object) -> object:
        self.name = name
        self.age = age


class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed


class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color


class AnimalFactory:  # фабричный класс
    @staticmethod
    def create_animal(animal_type, **kwargs):
        if animal_type == 'Dog':
            return Dog(**kwargs)
        elif animal_type == 'Cat':
            return Cat(**kwargs)
        else:
            raise ValueError(f'Нет такого вида животного: {animal_type}')


if __name__ == '__main__':
    dog = AnimalFactory.create_animal('Dog', name='Fido', age=3, breed='Retriever')
    cat = AnimalFactory.create_animal('Cat', name='Whiskers', age=2, color='Black')
