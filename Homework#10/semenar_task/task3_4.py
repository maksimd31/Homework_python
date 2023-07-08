# task3
''
from random import randint

"""
📌 Напишите класс для хранения информации о человеке: ФИО, возраст и т.п. на ваш выбор.
📌 У класса должны быть методы birthday для увеличения возраста на год, full_name для вывода полного ФИО и т.п. на ваш выбор.
📌 Убедитесь, что свойство возраст недоступно для прямого изменения, но есть возможность получить текущий возраст.

"""


class Human:
    def __init__(self, name: object, age: object, male: object) -> object:
        self.name = name
        self.__age = age
        self.male = male

    def birthday(self):
        self.__age += 1

    def full_name(self):
        return self.name

    def get_birthday(self):
        return self.__age


# human1 = Human('ivan', 18, 'm')
# print(human1.birthday())
# print(human1.get_birthday())

# task4
"""
Задание No4
📌 Создайте класс Сотрудник.
📌 Воспользуйтесь классом человека из прошлого задания.
📌 У сотрудника должен быть:
○ шестизначный идентификационный номер
○ уровень доступа вычисляемый как остаток от деления суммы цифр id на семь
  
"""


class Personal(Human):  # Наследование

    def __init__(self, id_num, name, age, male, levl=0):
        super().__init__(name, age, male)
        self.id_num = id_num
        self.levl = levl

    def dostup(self):
        # lst = sum([int(i) for i in str(ll)]) % 7  # запись чисел в список
        # или
        lst = sum(map(int, list(str(self.id_num)))) % 7
        # lst_s = sum(lst)
        # print(lst_s)
        self.levl = sum([int(i) for i in str(self.id_num)]) % 7
        print(self.levl)
        return self.levl

    # или
    # def level_gen(self):
    #     self.


rnd = randint(10000, 999999)
ii = sum([int(i) for i in str(rnd)]) % 7
print(ii)

human3 = Personal(rnd, 'oleg', 30, 'flame')
print(human3.dostup())
print(human3.full_name())

print(f'Проверка {ii % 7}')
