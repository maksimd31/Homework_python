
# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.

import sys
from datetime import datetime


# __all__ = [] # метод добавления в инициализацию


def date_checker(arg_date):
    try:
        datetime.strptime(arg_date, '%Y-%m-%d')
        return "Дата корректна"
    except ValueError:
        return "Неверный формат даты"


if __name__ == '__main__':
    date = sys.argv[1]  # в этом месте вызываться с консоли через sys
    date_checker(date)
