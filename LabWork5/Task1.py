import re

def is_valid_date(date_str):

    # Проверка формата с помощью регулярного выражения
    if not re.match(r'^\d{2}/\d{2}/\d{4}$', date_str):
        return False

    # Разделение на день, месяц и год
    day, month, year = date_str.split('/')

    try:
        day = int(day)
        month = int(month)
        year = int(year)
    except ValueError:
        return False  # Если части не являются числами

    # Проверка диапазонов месяца и года
    if month < 1 or month > 12 or year < 1:
        return False

    # Проверка дней в месяце
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Учет високосного года для февраля
    if month == 2:
        is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        max_day = 29 if is_leap else 28
    else:
        max_day = month_days[month - 1]

    return 1 <= day <= max_day

def validate_date(date_str):
    if not is_valid_date(date_str):
        raise ValueError(f"Некорректная дата: {date_str}")
    return date_str
