from abc import ABC, abstractmethod

# Шаг 1: Объявление интерфейса Shape
class Shape(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

# Шаг 2: Реализация интерфейса для каждой фигуры
class Circle(Shape):
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color

    def accept(self, visitor):
        return visitor.visit_circle(self)

class Square(Shape):
    def __init__(self, size, color):
        self.size = size
        self.color = color

    def accept(self, visitor):
        return visitor.visit_square(self)

class Star(Shape):
    def __init__(self, area):
        self.area = area

    def accept(self, visitor):
        return visitor.visit_star(self)

# Шаг 3: Объявление интерфейса Visitor
class Visitor(ABC):
    @abstractmethod
    def visit_circle(self, circle):
        pass

    @abstractmethod
    def visit_square(self, square):
        pass

    @abstractmethod
    def visit_star(self, star):
        pass

# Шаг 4: Создание класса расширения функциональности для вычисления площади
class AreaVisitor(Visitor):
    def visit_circle(self, circle):
        return 3.14 * circle.radius ** 2

    def visit_square(self, square):
        return square.size ** 2

    def visit_star(self, star):
        return star.area

# Дополнительный шаг: Расширение функциональности для получения цвета
class ColorVisitor(Visitor):
    def visit_circle(self, circle):
        return circle.color

    def visit_square(self, square):
        return square.color

    def visit_star(self, star):
        return "yellow"

# Дополнительный шаг: Расширение функциональности для количества углов
class CornerVisitor(Visitor):
    def visit_circle(self, circle):
        return 0

    def visit_square(self, square):
        return 4

    def visit_star(self, star):
        return 5

# Использование:
if __name__ == "__main__":
    circle = Circle(5, "red")
    square = Square(7.0, "blue")
    star = Star(36.0)
    
    area_visitor = AreaVisitor()
    color_visitor = ColorVisitor()
    corner_visitor = CornerVisitor()

    print("Площадь круга: {:.1f}".format(circle.accept(area_visitor)))
    print("Площадь квадрата: {:.1f}".format(square.accept(area_visitor)))
    print("Площадь звезды: {:.1f}".format(star.accept(area_visitor)))

    print("Цвет круга: {}".format(circle.accept(color_visitor)))
    print("Цвет квадрата: {}".format(square.accept(color_visitor)))
    print("Цвет звезды: {}".format(star.accept(color_visitor)))

    print("Количество углов круга: {}".format(circle.accept(corner_visitor)))
    print("Количество углов квадрата: {}".format(square.accept(corner_visitor)))
    print("Количество углов звезды: {}".format(star.accept(corner_visitor)))
