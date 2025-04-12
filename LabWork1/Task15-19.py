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

