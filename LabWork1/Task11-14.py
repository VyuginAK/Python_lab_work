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


# Задание 8
def sort_by_triple_deviation(strings):
    """
    Сортировка строк по квадратичному отклонению между:
    - средним ASCII-кодом всей строки
    - максимальным средним ASCII-кодом троек символов
    """

    def calculate_deviation(s):
        if len(s) < 3:
            return 0

        # Среднее значение ASCII-кодов для всей строки
        avg_all = sum(ord(c) for c in s) / len(s)

        # Максимальное среднее для троек символов
        triples_avg = [
            (ord(s[i]) + ord(s[i + 1]) + ord(s[i + 2])) / 3
            for i in range(len(s) - 2)
        ]
        max_triple = max(triples_avg) if triples_avg else 0

        return (avg_all - max_triple) ** 2  # Квадратичное отклонение

    return sorted(strings, key=calculate_deviation)

