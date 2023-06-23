# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

list_num = [1, 1, 1, 2, 3, 3, 4, 5, 5, 5, 5, 6, 7, 7, 7, 7, 8, 8, 9, 10, 11]


def find_duplicates(lst):
    duplicates = set()  # создаем множества set и кладем туда дубликаты
    unique = set()  # уникальные значения
    for item in lst:
        if item in unique:
            duplicates.add(item)  # записываем дубликаты
        else:
            unique.add(item)  # иначе записываем уникальные
    return list(duplicates)  #


print(find_duplicates(list_num))
