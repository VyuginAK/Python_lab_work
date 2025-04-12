# Задание №5
def max_cyrillic_sequence(s):
    max_count = 0  # Максимальная длина последовательности
    current = 0  # Текущая длина последовательности

    for char in s:
        # Проверяем, является ли символ кириллическим
        is_cyrillic = ('А' <= char <= 'Я') or ('а' <= char <= 'я') or (char in 'Ёё')

        if is_cyrillic:
            current += 1
            max_count = max(max_count, current)
        else:
            current = 0  # Сбрасываем счетчик
    return max_count

