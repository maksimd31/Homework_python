# 2. Прочитайте созданный в прошлом задании csv файл без использования
# csv.DictReader. Распечатайте его как pickle строку.

import csv
import pickle


# Без использования
def read_picl_print(arg_file):
    with open(arg_file, 'r') as f:
        reader = csv.reader(f)
        rows = list(reader)
    return pickle.dumps(rows)


def reed_csv_print(arg_file):
    """Выводит содержимое файла"""
    # data = []
    with open(arg_file, 'r') as f:
        reader = csv.reader(f)
        # for rows in reader:
        #     data.append(rows)
        output_to_the_screen(reader)


def output_to_the_screen(arg_print):
    """ Выводит на экран в столбик"""
    for i in arg_print:
        print(i)


if __name__ == '__main__':
    print(read_picl_print('./task1/data.csv'))
    reed_csv_print('./task1/data.csv')
else:
    __add_ = ['read_picl_print', "reed_csv_print"]
