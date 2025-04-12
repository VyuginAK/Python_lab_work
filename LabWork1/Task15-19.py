# Задание 5
def is_global_min(arr, index):

    if index < 0 or index >= len(arr):
        return False  # Некорректный индекс

    # Находим минимальный элемент массива
    global_min = min(arr)
    # Сравниваем элемент по индексу с глобальным минимумом
    return arr[index] == global_min

# Пример использования
arr = [5, 3, 1, 4, 2]
index = 2
print(f"Элемент {arr[index]} по индексу {index} является глобальным минимумом:", is_global_min(arr, index))


# Задание 17
def swap_min_max(arr):

    if len(arr) < 2:
        return arr  # Невозможно поменять

    # Находим индексы минимума и максимума
    min_index = arr.index(min(arr))
    max_index = arr.index(max(arr))

    # Меняем местами
    arr[min_index], arr[max_index] = arr[max_index], arr[min_index]
    return arr

# Пример использования
arr = [3, 1, 4, 6, 5]
print("После обмена:", swap_min_max(arr))


# Задание 29
def is_max_in_range(arr, a, b):

    if not arr:
        return False  # Пустой массив

    max_value = max(arr)
    return a <= max_value <= b

# Пример использования
arr = [7, 2, 10, 4, 5]
a, b = 8, 12
print(f"Максимум в интервале [{a}, {b}]:", is_max_in_range(arr, a, b))


# Задание 41
def average_of_abs(arr):

    if not arr:
        return 0  # Пустой массив

    # Сумма модулей элементов
    sum_abs = sum(abs(x) for x in arr)
    return sum_abs / len(arr)

# Пример использования
arr = [-3, 5, -2, 7]
print("Среднее модулей:", round(average_of_abs(arr), 2))


# Задание 53
def filter_elements(arr):

    if len(arr) < 2:
        return []

    avg = sum(arr) / len(arr)  # Среднее арифметическое
    max_val = max(arr)  # Максимальное значение

    # Фильтруем элементы
    return [x for x in arr if avg < x < max_val]

# Пример использования
arr = [4, 2, 9, 5, 7, 10, 8]
print("Отфильтрованный список:", filter_elements(arr))
