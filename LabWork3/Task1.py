import math


# Создаем кастомное исключение для отрицательных сторон
class NegativeSideLengthError(ValueError):
    def __init__(self, value, message="Сторона не может быть <= 0. Неверное значение: "):
        self.value = value
        super().__init__(message + str(value))


# Класс для треугольника (T1)
class Triangle:
    def __init__(self, side, identifier, x=0, y=0):
        if side <= 0:
            raise NegativeSideLengthError(side)
        self.__side = side  # Длина стороны
        self.__id = identifier  # Уникальный идентификатор
        self.__x = x  # Координата X центра
        self.__y = y  # Координата Y центра

    # Перемещение фигуры
    def move(self, dx, dy):
        self.__x += dx
        self.__y += dy

    # Расчет границ для проверки пересечений
    def get_bounding_box(self):
        h = (math.sqrt(3) / 2) * self.__side  # Высота равностороннего треугольника
        return (
            self.__x - self.__side / 2,  # Левый X
            self.__y - h / 2,  # Нижний Y
            self.__x + self.__side / 2,  # Правый X
            self.__y + h / 2  # Верхний Y
        )

    def get_id(self):
        return self.__id


# Класс для прямоугольника (T2)
class Rectangle:
    def __init__(self, width, height, identifier, x=0, y=0):
        if width <= 0 or height <= 0:
            raise NegativeSideLengthError(min(width, height))
        self.__width = width  # Ширина
        self.__height = height  # Высота
        self.__id = identifier  # Уникальный идентификатор
        self.__x = x  # Координата X центра
        self.__y = y  # Координата Y центра

    # Перемещение фигуры
    def move(self, dx, dy):
        self.__x += dx
        self.__y += dy

    # Расчет границ
    def get_bounding_box(self):
        return (
            self.__x - self.__width / 2,  # Левый X
            self.__y - self.__height / 2,  # Нижний Y
            self.__x + self.__width / 2,  # Правый X
            self.__y + self.__height / 2  # Верхний Y
        )

    def get_id(self):
        return self.__id


# Проверка пересечения двух фигур через их границы
def is_intersect(shape1, shape2):
    box1 = shape1.get_bounding_box()
    box2 = shape2.get_bounding_box()

    # Проверка пересечения по оси X
    x_overlap = (box1[0] <= box2[2]) and (box1[2] >= box2[0])

    # Проверка пересечения по оси Y
    y_overlap = (box1[1] <= box2[3]) and (box1[3] >= box2[1])

    return f"{shape1.get_id()} и {shape2.get_id()} {'пересекаются' if x_overlap and y_overlap else 'не пересекаются'}"


# Демонстрация работы
def main():
    try:
        # Создаем фигуры
        triangle = Triangle(4, "Треугольник", 0, 0)
        rectangle = Rectangle(5, 3, "Прямоугольник", 3, 0)

        # Исходное положение
        print("В исходном положении:", is_intersect(triangle, rectangle))  # Пересекаются

        # Перемещаем треугольник
        triangle.move(2, 0)
        print("После перемещения треугольника:",is_intersect(triangle, rectangle))  # Пересекаются

        # Перемещаем прямоугольник
        rectangle.move(0, 5)
        print("После перемещения прямоугольника:", is_intersect(triangle, rectangle))  # Не пересекаются

    except NegativeSideLengthError as e:
        print("Ошибка создания фигуры:", e)


if __name__ == "__main__":
    main()