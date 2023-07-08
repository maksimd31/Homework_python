# task2
''
"""
Возьмите задачу из прошлых семинаров (например сериализация
данных), которые вы уже решали. Превратите функции в методы класса, а параметры в свойства. 
Задачи должны решаться через вызов методов экземпляра. 
"""


class Task2:
    def __init__(self, arg_int=0):
        self.__arg_int = arg_int

    def search_for_a_prime_number_ver_3(self):
        """Функция нахождения простого числа Улучшенная версия №3 """
        if 0 <= self.__arg_int <= 100000:
            for i in range(2, int(self.__arg_int ** 0.5) + 1):
                if self.__arg_int % i == 0:
                    return "Число составное"
            else:
                return "Число простое"
        else:
            return "Число должно быть положительным и не превышать 100,000"


if __name__ == '__main__':
    p1 = Task2(232344433332323)
    print(f'p1 = {p1.search_for_a_prime_number_ver_3()}')
    p2 = Task2()
    print(f'p2 = {p2.search_for_a_prime_number_ver_3()}')

