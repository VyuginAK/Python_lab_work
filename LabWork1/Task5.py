import re

def find_dates(text):
    # Создаем шаблон для поиска даты:
    # - \d{1,2}  : день (1 или 2 цифры)
    # - (января|февраля|...) : название месяца в родительном падеже
    # - \d{4}    : год (4 цифры)
    pattern = r'\b(\d{1,2})\s+(января|февраля|марта|апреля|мая|июня|июля|августа|сентября|октября|ноября|декабря)\s+(\d{4})\b'

    # Ищем все совпадения в тексте
    dates = re.findall(pattern, text)

    # Объединяем найденные группы в строки формата 'день месяц год'
    result = [' '.join(date) for date in dates]
    return result

# Пример использования
text = "События произошли 5 мая 2023 и 31 февраля 2024. Также упоминается декабрь 2020, а также 5 июля того же года."
found_dates = find_dates(text)
print("Найденные даты:", found_dates)