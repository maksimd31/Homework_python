import Package_HM6.task1 as t1
import Package_HM6.task2_task3 as t2_3

# Задание 1
# Не знаю как правильно записать
# вариант записи 1
# date = str(input('Введите фату формата 2000-01-20\nВвод: '))
# print(Package_HM6.task1.date_checker(date))

# Вариант записи 2 мне такая запись понятнее
date = str(input('Введите фату формата 2000-01-20\nВвод: '))
print(t1.date_checker(date))

# Задание 2-3 в одном
print(t2_3.queen_8(8))

if __name__ == '__main__':
    # Задание 1
    print(f'Истина вывод {t1.date_checker("2002-12-21")}')  # Истина
    print(f"Лож вывод {t1.date_checker('2002-1')}")  # лож

    # Задание 2-3


