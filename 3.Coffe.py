# Интерфейс компонента
class Coffee:
    def cost(self):
        pass

# Реализация конкретного компонента - базовой чашки кофе
class SimpleCoffee(Coffee):
    def cost(self):
        return 5  # Базовая цена чашки кофе

# Абстрактный класс декоратора
class CoffeeDecorator(Coffee):
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost()

# Реализация конкретных декораторов - добавок к кофе
class MilkDecorator(CoffeeDecorator):
    def cost(self):
        return super().cost() + 2  # Добавляем стоимость молока

class SugarDecorator(CoffeeDecorator):
    def cost(self):
        return super().cost() + 1  # Добавляем стоимость сахара

class VanillaDecorator(CoffeeDecorator):
    def cost(self):
        return super().cost() + 3  # Добавляем стоимость ванильного сиропа

# Пример использования
if __name__ == "__main__":
    simple_coffee = SimpleCoffee()
    print(f"Цена простой чашки кофе: ${simple_coffee.cost()}")

    milk_coffee = MilkDecorator(simple_coffee)
    print(f"Цена чашки кофе с молоком: ${milk_coffee.cost()}")

    sugar_vanilla_coffee = VanillaDecorator(SugarDecorator(simple_coffee))
    print(f"Цена чашки кофе с сахаром и ванилью: ${sugar_vanilla_coffee.cost()}")
