from enum import Enum

# Интерфейс для пончика
class Donut:
    def eat(self):
        pass

# Классы конкретных видов пончиков
class CherryDonut(Donut):
    def eat(self):
        print("Мммм, это пончик с вишней")

class ChocolateDonut(Donut):
    def eat(self):
        print("Оооо, это шоколадный пончик")

class CustardDonut(Donut):
    def __init__(self):
        self.calorie = "Много"

    def eat(self):
        print("Уж ты, любимый пончик Леонида с заварным кремом")

# Перечисление для типов пончиков
class DonutType(Enum):
    cherry = 1
    chocolate = 2
    custard = 3

# Фабрика пончиков
class DonutFactory:
    def bake(self, donut_type):
        if donut_type == DonutType.cherry:
            return CherryDonut()
        elif donut_type == DonutType.chocolate:
            return ChocolateDonut()
        elif donut_type == DonutType.custard:
            return CustardDonut()

# Главная функция
def main():
    donut_factory = DonutFactory()

    # Заказ пончика для Леонида
    donut_for_leonid = donut_factory.bake(DonutType.custard)

    # Попробовать пончик
    donut_for_leonid.eat()

    # Вывести информацию о калорийности
    print(f"Калорийность: {donut_for_leonid.calorie}")

if __name__ == "__main__":
    main()
