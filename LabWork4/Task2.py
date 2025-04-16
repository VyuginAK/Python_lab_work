import re

# Чтение исходного файла
with open('input.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Разделение текста на предложения, сохраняя знаки окончания
sentences = re.findall(r'[^.!]*[.!]', text)
processed_sentences = []

for sent in sentences:
    if not sent:  # Пропускаем пустые строки
        continue

    # Извлекаем знак окончания предложения (последний символ)
    ending = sent[-1] if sent[-1] in ('.', '!') else ''
    # Основная часть предложения (без окончания)
    content = sent[:-1] if ending else sent

    # Разбиваем на слова по пробелам
    words = content.split()

    # Удаляем подряд идущие дубликаты
    filtered_words = []
    previous_word = None
    for word in words:
        if word != previous_word:
            filtered_words.append(word)
            previous_word = word

    # Собираем предложение обратно
    new_content = ' '.join(filtered_words)
    # Добавляем знак окончания
    new_sentence = new_content + ending
    processed_sentences.append(new_sentence)

# Объединяем обработанные предложения в текст
new_text = '\n'.join(processed_sentences)

# Запись результата в новый файл
with open('output.txt', 'w', encoding='utf-8') as f:
    f.write(new_text)