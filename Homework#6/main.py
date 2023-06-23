import Package_HM6.task1 as t1
import Package_HM6

# Не знаю как правильно записать

# вариант записи 1
# date = str(input('Введите фату формата 2000-01-20\nВвод: '))
# print(Package_HM6.task1.date_checker(date))

# Вариант записи 2
date = str(input('Введите фату формата 2000-01-20\nВвод: '))
print(t1.date_checker(date))

if __name__ == '__main__':
    print(f'Истина вывод {t1.date_checker("2002-12-21")}')  # Истина
    print(f"Лож вывод {t1.date_checker('2002-1')}")  # лож
