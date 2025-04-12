import random
# Задание №5
def shuffle_string(s):
    # Преобразуем строку в список символов
    chars = list(s)
    # Перемешиваем список символов
    random.shuffle(chars)
    # Объединяем список обратно в строку
    return ''.join(chars)

# Пример использования
original = "Hello, World!"
shuffled = shuffle_string(original)
print("Перемешанная строка:", shuffled)


# Задание №7
def is_uppercase_palindrome(s):
    # Собираем все прописные символы из строки
    uppercase_chars = [char for char in s if char.isupper()]
    # Проверяем, равен ли список своему обратному варианту
    return uppercase_chars == uppercase_chars[::-1]

# Пример использования
test_str = "AbiuC AcCkhAf"
result = is_uppercase_palindrome(test_str)
print("Прописные символы образуют палиндром?", result)


# Задание 14
def sort_words_by_length(s):
    # Разбиваем строку на список слов
    words = s.split()
    # Сортируем слова по их длине
    sorted_words = sorted(words, key=lambda x: len(x))
    # Объединяем отсортированные слова обратно в строку
    return ' '.join(sorted_words)

# Пример использования
input_str = "In this sentence the words are in order"
sorted_str = sort_words_by_length(input_str)
print("Слова, отсортированные по длине:", sorted_str)