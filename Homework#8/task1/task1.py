# 1. Напишите функцию, которая преобразует pickle файл хранящий список словарей в табличный csv файл. Для тестированию
#    возьмите pickle версию файла из предыдущей задачи. Функция должна извлекать ключи словаря для заголовков столбца из
#    переданного файла.

import pickle
import csv

# для проверки создаем словарь pickle
data = [
    {'name': 'Иван', 'age': 25, 'city': 'Москва'},
    {'name': 'Инна', 'age': 30, 'city': 'Клин'},
    {'name': 'Олег', 'age': 35, 'city': 'Волоколамск'}
]


# Записываем его в бинарный файл
with open('data.pickle', 'wb') as f:
    pickle.dump(data, f)


def pickle_to_csv(pickle_file, csv_file):
    """Функция преобразования файла"""
    with open(pickle_file, 'rb') as f_to:
        data_to = pickle.load(f_to)

    headers = list(data_to[0].keys())

    with open(csv_file, 'w', newline='') as f_to:
        writer = csv.writer(f_to)
        writer.writerow(headers)
        for row in data_to:
            writer.writerow(list(row.values()))

    print('Файл успешно преобразован в CSV формат')


def main(pickle_arg='data.pickle', csv_arg='data.csv'):
    pickle_to_csv(pickle_arg, csv_arg)


#

if __name__ == '__main__':
    main()
else:
    __add__ = ['pickle_to_csv']
