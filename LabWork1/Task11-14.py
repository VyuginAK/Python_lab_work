import statistics

# Задание №2
def sort_by_avg_ascii(strings):

    def get_avg(s):
        # Считаем сумму ASCII-кодов всех символов и делим на длину строки
        return sum(ord(char) for char in s) / len(s) if s else 0

    # Сортируем строки по вычисленному среднему значению
    return sorted(strings, key=get_avg)

# Задание 6
def sort_by_median_ascii(strings):

    def get_median(s):
        # Преобразуем символы в ASCII-коды и находим медиану
        codes = [ord(char) for char in s]
        return statistics.median(codes) if codes else 0

    return sorted(strings, key=get_median)

