# Чтение списка строк с клавиатуры
lines = []
print("Введите строки (для завершения введите пустую строку):")
while True:
    line = input()
    if line == "":
        break
    lines.append(line)

# Сортируем строки по количеству слов в каждой
sorted_by_words = sorted(lines, key=lambda x: len(x.split()))

# Выводим результат
print("\nСтроки, отсортированные по количеству слов:")
for line in sorted_by_words:
    word_count = len(line.split())  # Считаем количество слов в текущей строке
    print(f"'{line}' (слов: {word_count})")