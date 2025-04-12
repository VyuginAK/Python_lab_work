import math

# Находит количество делителей числа n, которые не делятся на 3
def count_non_divisible_by_3(n):
    if n <= 0:
        return 0  # Отрицательные числа и 0 не имеют натуральных делителей
    count = 0  # Счётчик делителей

    # Перебираем возможные делители от 1 до корня из n
    for i in range(1, int(math.isqrt(n)) + 1):
        if n % i == 0:  # Если i — делитель n
            if i % 3 != 0:  # Если делитель не делится на 3
                count += 1
            counterpart = n // i  # Парный делитель (например, для 12: 3 и 4)
            if counterpart != i and counterpart % 3 != 0:  # Проверяем парный делитель
                count += 1
    return count

 # Находит минимальную нечётную цифру в числе n. Возвращает -1, если таких цифр нет
def min_odd_digit(n):
    n = abs(n)  # Работаем с модулем числа (чтобы избежать проблем с отрицательными числами)
    min_digit = None  # Пока не нашли ни одной нечётной цифры

    for digit_str in str(n):  # Перебираем каждую цифру в числе (как строку)
        digit = int(digit_str)  # Преобразуем в число
        if digit % 2 != 0:  # Если цифра нечётная
            if min_digit is None or digit < min_digit:  # Если это первая нечётная или меньше найденной
                min_digit = digit

    return min_digit if min_digit is not None else -1  # Возвращаем -1, если нечётных цифр нет
