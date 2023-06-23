# Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: «Число является простым,
# если делится нацело только на единицу и на себя».
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.


number_1 = int(input("Введите число: "))


def search_for_a_prime_number(number):
    """Функция нахождения простого числа """
    if number < 0 or number > 100000:
        print("Число должно быть положительным и не превышать 100,000")
    else:
        is_prime_flag = True
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                is_prime_flag = False
                break
        if is_prime_flag:
            print("Число простое")
        else:
            print("Число составное")


search_for_a_prime_number(number_1)


def search_for_a_prime_number_ver_2(number):
    """Функция нахождения простого числа Улучшенная версия №2 """
    if 0 <= number <= 100000:
        is_prime_flag = True
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                is_prime_flag = False
                break
        if is_prime_flag:
            print("Число простое")
        else:
            print("Число составное")
    else:
        print("Число должно быть положительным и не превышать 100,000")


search_for_a_prime_number_ver_2(number_1)


def search_for_a_prime_number_ver_3(number):
    """Функция нахождения простого числа Улучшенная версия №3 """
    if 0 <= number <= 100000:
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                print("Число составное")
                break
        else:
            print("Число простое")
    else:
        print("Число должно быть положительным и не превышать 100,000")


search_for_a_prime_number_ver_3(number_1)
