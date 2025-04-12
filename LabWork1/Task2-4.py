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
# Задание 14
def sort_words_by_length(s):
    # Разбиваем строку на список слов
    words = s.split()
    # Сортируем слова по их длине
    sorted_words = sorted(words, key=lambda x: len(x))
    # Объединяем отсортированные слова обратно в строку
    return ' '.join(sorted_words)
