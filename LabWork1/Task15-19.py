# Задание 5
def is_global_min(arr, index):

    if index < 0 or index >= len(arr):
        return False  # Некорректный индекс

    # Находим минимальный элемент массива
    global_min = min(arr)
    # Сравниваем элемент по индексу с глобальным минимумом
    return arr[index] == global_min

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

# Задание 29
def is_max_in_range(arr, a, b):

    if not arr:
        return False  # Пустой массив

    max_value = max(arr)
    return a <= max_value <= b

# Задание 41
def average_of_abs(arr):

    if not arr:
        return 0  # Пустой массив

    # Сумма модулей элементов
    sum_abs = sum(abs(x) for x in arr)
    return sum_abs / len(arr)

