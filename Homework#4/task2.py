# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента. Если ключ не хешируем,
# используйте его строковое представление.

# Изменяемые объекты
list_1 = (6, 7)  # кортеж
dict_ = {6: 7, 7: 2}  # кортеж
set_ = set[1, 2, 3, 4, 5]
int_ = 1, 2, 3, 45


def task_2_2(**kwargs):
    result = {}
    for key, value in kwargs.items():
        if not hash(key):
            key = str(key)
        result[key] = value
    return result


print(task_2_2(key=list_1, valie='hhghjj'))
print(task_2_2(key=dict_, valie='hhghjj'))
print(task_2_2(key=set_, valie='hhghjj'))
print(task_2_2(key=int_, valie='hhghjj'))

if __name__ == " __main__":
    print(task_2_2(key=list_1, valie='hhghjj'))
    print(task_2_2(key=dict_, valie='hhghjj'))
    print(task_2_2(key=set_, valie='hhghjj'))
    print(task_2_2(key=int_, valie='hhghjj'))
