#
# ✔ Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.
# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное
# строковое представление. Функцию hex используйте для проверки своего результата.


# ВАЖНО
# Я писал решение довольно долго, и у меня слетала операционка, и все пропало, поэтому сдаю все с опозданием,
# полюс нужно успеть сделать следующе дз, задание с банком тоже слетело.
# К сожелению ч 3 дня не пушил в гит изменения, и очень этому расстроился, но это урок(теперь все храню в гит)

# В задание с банком я делал базу клиентов с хранением в sqlit3 и в, вложенных словарях
# (тут я дико запутался, поскольку мне нужно ыло взять данные из словаря обработать их и вернуть обратно в словарь).
# Поэтому я начал делать все через sqlit3, ну и все слетело, осталось только первоначальное решение


dict_ras = {'10': 'a', '11': 'b', '12': 'c', '13': 'd', '14': 'e', '15': 'f'}

num = 171  # число
step = 16  # степень


def dict123(arg, arg_dict):
    """ Функция поиска по словарю """
    if arg in arg_dict:
        return arg_dict.get(arg)


def convert(arg_num, arg_step):
    """ Функция более тривиальная она возвращает только цифры"""
    result = ''
    while arg_num > 0:
        result = str(arg_num % arg_step) + result
        arg_num = arg_num // arg_step
    return result


print(convert(num, step))


def the_first_stream(arg_result,arg_num,arg_step):
    return str(arg_num % arg_step) + arg_result


def convert_2(arg_num, arg_step, arg_dict):
    """"Эта функция №2 которая возвращает более правильные ответы,
    а именно буквы согласно правилами конвертирования они указаны в словаре"""
    converted_list = []
    result = ''
    while arg_num > 0:
        # result = str(arg_num % arg_step) + result
        result = the_first_stream(result,arg_num,arg_step)
        if len(result) >= 2:
            rr = dict123(result[0:2], arg_dict)
            converted_list.append(rr)
            converted_list.reverse()
            # list_concatenation = ','.join(converted_list)
        arg_num //= arg_step
    if len(result) > 2:
        list_concatenation = ','.join(converted_list)
        print(list_concatenation)
    else:
        print(result)


# Тут довольно долго мучался что бы сделать все по уму
convert_2(num, step, dict_ras)
