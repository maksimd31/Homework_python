# ✔ Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.
# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное
# строковое предс

def to_hex(num):
    hex_digits = "0123456789ABCDEF"
    result = ""
    while num > 0:
        quotient = num // 16
        remainder = num % 16
        result = hex_digits[remainder] + result
        num = quotient
    return result


print(to_hex(1011))
print(hex(1011))
# Готово
