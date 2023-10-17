'''
� Создайте модуль и напишите в нём функцию, которая
получает на вход дату в формате DD.MM.YYYY
� Функция возвращает истину, если дата может существовать
или ложь, если такая дата невозможна.
� Для простоты договоримся, что год может быть в диапазоне
[1, 9999].
� Весь период (1 января 1 года - 31 декабря 9999 года)
действует Григорианский календарь.
� Проверку года на високосность вынести в отдельную
защищённую функцию.
'''

__all__ = ['is_valid_date']


def is_valid_date(date_str: str) -> bool:
    day, month, year = map(int, date_str.split('.'))

    # Проверка диапазона года
    if year < 1 or year > 9999:
        return False

    # Проверка диапазона месяца
    if month < 1 or month > 12:
        return False

    # Проверка диапазона дня
    if day < 1 or day > 31:
        return False

    # Проверка месяцев с 30 днями
    if month in [4, 6, 9, 11] and day > 30:
        return False

    # Проверка февраля
    if month == 2:
        if _is_leap_year(year):
            if day > 29:
                return False
        else:
            if day > 28:
                return False

    return True


def _is_leap_year(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True


if __name__ == '__main__':
    print(is_valid_date(input('введите дату в формате DD.MM.YYYY ')))
