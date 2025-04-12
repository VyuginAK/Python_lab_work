# Чтение списка строк с клавиатуры
lines = []
print("Введите строки (для завершения нажмите Enter):")
while True:
    line = input()  # Читаем ввод пользователя
    if line == "":  # Если введена пустая строка, завершаем ввод
        break
    lines.append(line)  # Добавляем строку в список

# Сортируем строки по длине (от самой короткой к самой длинной)
sorted_by_length = sorted(lines, key=lambda x: len(x))

# Выводим результат
print("\nСтроки, отсортированные по длине:")
for line in sorted_by_length:
    print(f"'{line}' (длина: {len(line)})")