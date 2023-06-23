# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти

# ✔ Сумма пополнения и снятия кратны 50 у.е.

# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.

# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%

# ✔ Нельзя снять больше, чем на счёте

# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег


def markup_tax():
    """При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной"""
    pass


def withdrawal_percentage():
    """Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е"""
    pass


def third_operation():
    """После каждой третей операции пополнения или снятия начисляются проценты - 3% """
    pass


def multiple_of_50():
    """Сумма пополнения и снятия кратны 50 у.е."""
    pass


def replenishment(arg_check):
    """ Пополнение """
    introduction = input('Кау сумму хотите внести?')
    return arg_check + introduction


def withdrawal():
    """ Снятие """
    pass


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

match answer:
    case 1:
        replenishment(start_sum)
    case 0:
        print('Выход')






def balance(start_balance, operations):
    balance = start_balance
    withdrawal_count = 0
    deposit_count = 0

    for i, (operation_type, amount) in enumerate(operations):
        if operation_type == 'withdrawal':
            if amount > balance:
                print(f"Нельзя снять {amount} у.е.: недостаточно средств на счете")
            elif amount % 50 != 0:
                print(f"Нельзя снять {amount} у.е.: не кратно 50")
            else:
                balance -= amount
                withdrawal_count += 1
                if withdrawal_count % 3 == 0:
                    balance *= 0.97
                if balance > 5000000:
                    balance *= 0.9
                if amount * 0.015 > 30:
                    fee = amount * 0.015
                else:
                    fee = 30
                if fee > 600:
                    fee = 600
                balance -= fee
        elif operation_type == 'deposit':
            if amount % 50 != 0:
                print(f"Нельзя пополнить на {amount} у.е.: не кратно 50")
            else:
                balance += amount
                deposit_count += 1
                if deposit_count % 3 == 0:
                    balance *= 1.03
                if balance > 5000000:
                    balance *= 0.9
        else:
            print(f"Неизвестный тип операции: {operation_type}")
        print(f"Баланс после операции {i+1}: {balance} у.е.")

    return balance
