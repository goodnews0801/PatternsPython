from abc import ABC, abstractmethod

# Шаг 1: Объявление интерфейса Animal
class Animal(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

# Шаг 2: Реализация интерфейса для каждого класса животного
class Monkey(Animal):
    def shout(self):
        print("У-у-у аaaaaаa!")

    def accept(self, visitor):
        visitor.visit_monkey(self)

class Lion(Animal):
    def roar(self):
        print("Рррррррррр!")

    def accept(self, visitor):
        visitor.visit_lion(self)

class Dolphin(Animal):
    def speak(self):
        print("Пиу пиу пиу")

    def accept(self, visitor):
        visitor.visit_dolphin(self)

# Шаг 3: Объявление интерфейса Visitor
class Visitor(ABC):
    @abstractmethod
    def visit_monkey(self, monkey):
        pass

    @abstractmethod
    def visit_lion(self, lion):
        pass

    @abstractmethod
    def visit_dolphin(self, dolphin):
        pass

# Шаг 4: Создание класса расширения функциональности
class SoundVisitor(Visitor):
    def visit_monkey(self, monkey):
        print("Вы подошли к клетке с Обезьянкой:")
        monkey.shout()

    def visit_lion(self, lion):
        print("Вы подошли к клетке со Львом:")
        lion.roar()

    def visit_dolphin(self, dolphin):
        print("Вы подошли к бассейну с Дельфином:")
        dolphin.speak()

# Использование:
if __name__ == "__main__":
    monkey = Monkey()
    lion = Lion()
    dolphin = Dolphin()
    sound_visitor = SoundVisitor()

    monkey.accept(sound_visitor)
    print()
    lion.accept(sound_visitor)
    print()
    dolphin.accept(sound_visitor)
