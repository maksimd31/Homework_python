# Напишите функцию для транспонирования матрицы
# Я не понимаю как это работает и удивлен, что на семинаре ни у кого не было вопросов

matrix = [[1, 2], [3, 4]]


def matrix_transpositions(arg):
    convert_matrix = zip(*arg)  # но работает только при равносторонней матрице,
    # то есть будет работать до самого короткой строкой матрицы
    return tuple(convert_matrix)  # выводим список кортежей
    # for i in convert_matrix:
    #     return print(i)


matrix_transpositions(matrix)
