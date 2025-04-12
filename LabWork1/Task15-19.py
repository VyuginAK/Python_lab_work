# Задание 5
def is_global_min(arr, index):

    if index < 0 or index >= len(arr):
        return False  # Некорректный индекс

    # Находим минимальный элемент массива
    global_min = min(arr)
    # Сравниваем элемент по индексу с глобальным минимумом
    return arr[index] == global_min

