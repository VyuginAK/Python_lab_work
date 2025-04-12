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
