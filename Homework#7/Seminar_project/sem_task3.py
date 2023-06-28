# Задание №3
# ✔ Напишите функцию, которая открывает на чтение созданные в прошлых задачах файлы с числами и именами.
# ✔ Перемножьте пары чисел. В новый файл сохраните имя и произведение:
# ✔ если результат умножения отрицательный, сохраните имя записанное строчными буквами и произведение по модулю
# ✔ если результат умножения положительный, сохраните имя прописными буквами и произведение округлённое до целого.
# ✔ В результирующем файле должно быть столько же строк, сколько в более длинном файле.
# ✔ При достижении конца более короткого файла, возвращайтесь в его начало.
__all__ = ["task_3"]


def task_3(names, numbers):
    result = '../result.txt'
    with(
        open(names, 'r', encoding='utf-8') as f_1,
        open(numbers, 'r', encoding='utf-8') as f_2,
        open(result, 'w', encoding='utf-8') as f_3
    ):
        results_mult = []
        for line in f_2:
            a, b = map(float, line.strip().split('|'))
            results_mult.append(a * b)
        list_names = []
        for line in f_1:
            list_names.append(line.strip())

        res_list = []
        # перебираем списки. список меньшего размера перебирается циклически
        for i in range(max(len(results_mult), len(list_names))):
            res_mult = results_mult.pop(0)
            results_mult.append(res_mult)
            name = list_names.pop(0)
            list_names.append(name)
            if res_mult <= 0:
                res_list.append(f'{name.lower()}-{abs(res_mult)}')
            else:
                res_list.append(f'{name.upper()}-{int(res_mult)}')
        # Построчная запись в результирующий файл
        for line in res_list:
            print(line, file=f_3)


if __name__ == '__main__':
    names = '../names_main.txt'
    numbers = '../numbers_main.txt'
    task_3(names, numbers)
