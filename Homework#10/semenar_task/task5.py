# tt
''
"""
📌 Создайте три (или более) отдельных классов животных. Например рыбы, птицы и т.п.
📌 У каждого класса должны быть как общие свойства, например имя, так и специфичные для класса.
📌 Для каждого класса создайте метод, выводящий информацию специфичную для данного класса.
   
"""


class Animal:
    def __init__(self, name: object, tail: object) -> object:
        self.name = name
        self.tail = tail

    def name_animal(self):
        return self.name


class Fish(Animal):
    def __init__(self, deep, fresh_water, name, tail):
        super().__init__(name, tail)
        self.name = name
        self.fresh_water = fresh_water
        self.deep = deep

    def get_spec(self):
        if self.fresh_water:
            return True
        else:
            return False

    def check_deep(self):
        if self.deep < 3:
            return 'Мелкая'
        elif 3 < self.deep < 15:
            return 'Среднее'
        else:
            return 'Крупно водный'


class Bird(Animal):
    WING = 0

    def __init__(self, wings, name, tail):
        super().__init__(name, tail)
        self.name = name
        self.wings = wings

    def get_spec_small_bird(self):
        small_wing = 20
        self.wings = small_wing / 2
        return self.wings


class Mammal(Animal):

    # ZIMA = 'zima'
    # LETO = 'leto'
    def __init__(self, hibernate, name, tail):
        super().__init__(name, tail)
        self.name = name
        self.hibernate = hibernate

    def get_spec(self):
        if self.hibernate:
            return True
        else:
            return False
