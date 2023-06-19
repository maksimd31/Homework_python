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


balance = 0
count_operation = 0


# Решение через строки
def deposit(amount):
    """Пополнение / после 3 операции начисляются проценты/ проверка на богатство"""
    global balance, count_operation
    balance += amount
    count_operation += 1
    if count_operation % 3 == 0:
        balance += balance * 0.03
    if balance > 5000000:
        balance -= balance * 0.1
    return f"Текущий баланс: {balance}"


def withdraw(amount):
    """Снятие"""
    global balance, count_operation
    if amount > balance:
        print("На счете недостаточно средств")
        return
    commission = amount * 0.015 if amount * 0.015 >= 30 else 30
    if commission > 600:
        commission = 600
    balance -= amount + commission
    count_operation += 1
    if count_operation % 3 == 0:
        balance += balance * 0.03
    if balance > 5000000:
        balance -= balance * 0.1
    print(f"Текущий баланс: {balance}")


information_field = """
Действе над счетом
Введите нужное вам действие
1. Пополнение
2. Снятие
0. Выход

Выберите действие \nВвод:
"""
print(information_field)

choice = int(input("Ваш выбор: "))

while choice != 0:
    match choice:
        case 1:
            amount = int(input("Введите сумму для пополнения: "))
            if amount % 50 != 0:
                print("Сумма должна быть кратной 50 у.е.")
            else:
                deposit(amount)
                print('Пополнение успешно прошло')
                break
        case 2:
            amount = int(input("Введите сумму для снятия: "))
            if amount % 50 != 0:
                print("Сумма должна быть кратной 50 у.е.")
            else:
                withdraw(amount)
                break
        case 0:
            print("Выход")


# def choice_():
#     while choice != 0:
#         if choice == 1:
#             amount = int(input("Введите сумму для пополнения: "))
#             if amount % 50 != 0:
#                 print("Сумма должна быть кратной 50 у.е.")
#                 break
#             else:
#                 deposit(amount)
#                 print('Пополнение успешно прошло')
#                 break
#     if choice == 2:
#         amount = int(input("Введите сумму для снятия: "))
#         if amount % 50 != 0:
#             print("Сумма должна быть кратной 50 у.е.")
#         else:
#             withdraw(amount)
#     else:
#         print('Для выхода нажмите 0')
#
#
# choice_()
