# Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.


# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.

# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег

# пытался решить через словари по принципу одна функция выполняет одно действие, пытался сделать с принципами ООП

def create_new_input():
    """Функция для ввода """
    fio = input('Введите фио клиента')
    deposit_input = input('введите стартовый депозит')
    return fio, deposit_input


def create_dict_new_client(keys_fio, values_deposit, my_dict=dict):
    """Функция создает новый словарь и добавляет туда клиентов"""
    # my_dict = {}
    for i in range(len(keys_fio)):
        my_dict[keys_fio[i]] = values_deposit[i]
    return my_dict


information_field = """
Действе над счетом
Введите нужное вам действие
1. Пополнение
2. Снятие
0. Выход

Выберите действие \nВвод:
"""
start_sum = 0

answer = int(input(information_field))

dict_list = {"Иванов Иван Иванович": 0}


def five(arg):
    """Проверяет кратность 50"""
    if arg % 50 != 0:
        return False
    else:
        return True


# def five_next(arg):
#     if not five(arg):
#         return "Сумма не кратна 50\nПопробуйте еще раз\nДля выхода нажмите 0"


def dictionary_search(arg):
    """Поиск в списке"""
    for i in arg:
        return arg.get(i)


def changing_the_dictionary(arg, arg_sum, arg_input, arg_input_con):
    """Вносит изменения в список"""
    for i in arg:
        if arg_input_con:  # если 4 аргумент True, то это сложение
            arg[i] = arg_sum + arg_input
            result = arg[i]
            return result
        else:  # иначе False
            arg[i] = arg_sum - arg_input
            result = arg[i]
            return result


# def replenishment(arg):
#     """Пополнение, одна из первых версий функции"""
#     while True:
#         for i in arg:
#             summ = arg.get(i)
#             reed = int(input('Какую сумму вы хотите внести?'))
#             if not five(reed):
#                 print("Сумма не кратна 50\nПопробуйте еще раз\nДля выхода нажмите 0")
#             elif reed == 0:
#                 break
#             else:
#                 arg[i] = summ + reed
#                 result = arg[i]
#                 return result


# def withdrawal():
#     """Снятие"""
#     while True:
#         deposit_wi = dictionary_search(dict_list)
#         read_wi = int(input('Какую сумму вы хотите снять?'))


match answer:
    case 1:
        while True:
            """Пополнение тут я не знал как лучше сделать, с начала я сделал функции в которых было все, 
            но решил что одна функция должна выполнять одно действие, а в модуле case что то типа вьюшки где собрал
            все функции в одном месте и прописал логику их взаимоотношений"""
            # print(replenishment(dict_list))
            deposit = dictionary_search(dict_list)
            read = int(input('Какую сумму вы хотите внести?'))
            if not five(read):
                print("Сумма не кратна 50\nПопробуйте еще раз\nДля выхода нажмите 0")
            elif read == 0:
                break
            else:
                changing_the_dictionary(dict_list, deposit, read, True)

    case 2:
        """Снятие"""
        while True:
            deposit_wi = dictionary_search(dict_list)
            read_wi = int(input('Какую сумму вы хотите снять?'))
            if not five(read_wi):
                print("Сумма не кратна 50\nПопробуйте еще раз\nДля выхода нажмите 0")
            elif read_wi == 0:
                break
            else:
                changing_the_dictionary(dict_list, deposit_wi, read_wi, False)
    case 0:
        """Выход"""
        print('Выход')
