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

# Пример использования
text = "Привет! Это тестЁё для проверки"
print(max_cyrillic_sequence(text))


# Задание №7
def find_min_natural(s):
    min_num = None  # Начальное значение минимального числа
    current_num = ""  # Здесь будем собирать текущее число

    for char in s + " ":  # Добавляем пробел в конец для обработки последнего числа
        if char.isdigit():
            current_num += char  # Добавляем к текущему числу
        else:
            # Если собрали какое-то число
            if current_num:
                num = int(current_num)
                if num > 0:
                    # Если это первое найденное число или оно меньше текущего минимума
                    if min_num is None or num < min_num:
                        min_num = num
                current_num = ""  # Сбрасываем текущее число

    return min_num  # Возвращаем минимальное число (или None, если не нашли)

# Примеры использования
print(find_min_natural("В 5 корзинах 8 яблока и 12 апельсинов"))


# Задание №14
def max_digit_sequence(s):
    max_count = 0  # Максимальная длина последовательности
    current = 0  # Текущая длина последовательности

    for char in s:
        if char.isdigit():
            current += 1
            max_count = max(max_count, current)
        else:
            current = 0  # Сбрасываем счетчик

    return max_count

# Пример использования
text = "ABC12345def678ghij99999"
print(max_digit_sequence(text))