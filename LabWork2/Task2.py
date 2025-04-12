# Читаем количество строк
print("Введите количество строк: ")
n = int(input())

# Создаем словарь для подсчета слов
word_count = {}

# Обрабатываем каждую строку
print("Введите строки:")
for _ in range(n):
    line = input().strip()  # Удаляем лишние пробелы по краям
    words = line.split()  # Разбиваем строку на слова

    for word in words:
        # Увеличиваем счетчик для слова или устанавливаем 1, если его нет
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

# Находим максимальную частоту
max_count = max(word_count.values(), default=0)

# Собираем все слова с максимальной частотой
most_common = [word for word, count in word_count.items() if count == max_count]

# Сортируем лексикографически и выбираем первое
most_common_sorted = sorted(most_common)

# Выводим результат
print("Чаще всего встречается:", most_common_sorted[0] if most_common_sorted else "")