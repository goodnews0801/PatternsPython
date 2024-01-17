# Передача стратегии через функцию

# Функция, реализующая стратегию преобразования строки в нижний регистр
def low_cased_strategy(s):
    return s.lower()

# Класс Printer, который принимает стратегию в качестве параметра
class Printer:
    def __init__(self, print_strategy):
        self.print_strategy = print_strategy

    # Метод для вывода строки с использованием стратегии
    def print_str(self, s):
        print(self.print_strategy(s))

# Использование

# Создание объекта Printer с передачей стратегии в виде функции
printer1 = Printer(low_cased_strategy)
printer1.print_str("LalAlA")

# Создание объекта Printer с передачей стратегии в виде лямбда-функции
printer2 = Printer(lambda s: s.upper())
printer2.print_str("LalAlA")

# Создание объекта Printer с передачей стратегии в виде встроенной функции
printer3 = Printer(str.upper)
printer3.print_str("LalAlA")

# Передача стратегии через класс

# Базовый класс PrintStrategy с методом strategy, который должны реализовывать подклассы
class PrintStrategy:
    def strategy(self, s):
        pass

# Подкласс LowerPrintStrategy, реализующий стратегию преобразования строки в нижний регистр
class LowerPrintStrategy(PrintStrategy):
    def strategy(self, s):
        return s.lower()

# Класс Printer, принимающий объект стратегии в качестве параметра
class Printer:
    def __init__(self, print_strategy):
        self.print_strategy = print_strategy

    # Метод для вывода строки с использованием стратегии
    def print_str(self, s):
        print(self.print_strategy.strategy(s))

# Использование

# Создание объекта Printer с передачей стратегии в виде объекта класса
printer4 = Printer(LowerPrintStrategy())
printer4.print_str("LalAlA")
