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


def sum_special_divisors(n):
    """
    Находит сумму делителей числа n, которые:
    1. Взаимно просты с суммой цифр числа (НОД = 1).
    2. Не взаимно просты с произведением цифр числа (НОД > 1).
    """
    if n == 0:
        return 0  # У 0 бесконечно много делителей, но по условию пропускаем

    def sum_of_digits(num):  # Вспомогательная функция: сумма цифр
        return sum(int(d) for d in str(abs(num)))

    def product_of_digits(num):  # Вспомогательная функция: произведение цифр
        product = 1
        for d in str(abs(num)):
            product *= int(d)
        return product

    s = sum_of_digits(n)  # Сумма цифр числа
    p = product_of_digits(n)  # Произведение цифр числа

    # Находим все делители числа n
    divisors = set()
    for i in range(1, int(math.isqrt(abs(n))) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)

    total = 0  # Сумма подходящих делителей

    for d in divisors:
        # Проверяем, что НОД(d, сумма цифр) = 1
        if math.gcd(d, s) == 1:
            # Если произведение цифр = 0 (содержит 0), то любой d > 1 не взаимно прост с 0
            if p == 0:
                if d > 1:
                    total += d
            else:
                # Проверяем, что НОД(d, произведение цифр) > 1
                if math.gcd(d, p) != 1:
                    total += d
    return total
