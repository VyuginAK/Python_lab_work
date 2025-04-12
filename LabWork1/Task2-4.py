import random
# Задание №5
def shuffle_string(s):
    # Преобразуем строку в список символов
    chars = list(s)
    # Перемешиваем список символов
    random.shuffle(chars)
    # Объединяем список обратно в строку
    return ''.join(chars)
# Задание №7
def is_uppercase_palindrome(s):
    # Собираем все прописные символы из строки
    uppercase_chars = [char for char in s if char.isupper()]
    # Проверяем, равен ли список своему обратному варианту
    return uppercase_chars == uppercase_chars[::-1]
