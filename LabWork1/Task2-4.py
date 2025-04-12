import random
# Задание №5
def shuffle_string(s):
    # Преобразуем строку в список символов
    chars = list(s)
    # Перемешиваем список символов
    random.shuffle(chars)
    # Объединяем список обратно в строку
    return ''.join(chars)
