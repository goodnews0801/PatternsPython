class Burger:
    def __init__(self, burger_builder):
        # Инициализация бургера с ингредиентами из BurgerBuilder
        self.cheese = burger_builder.cheese
        self.pepperoni = burger_builder.pepperoni
        self.lettuce = burger_builder.lettuce
        self.tomato = burger_builder.tomato

    def display_burger(self):
        # Вывод информации о бургере
        print(f"Burger with Cheese: {self.cheese}, Pepperoni: {self.pepperoni}, Lettuce: {self.lettuce}, Tomato: {self.tomato}")

class BurgerBuilder:
    def __init__(self):
        # Инициализация параметров ингредиентов по умолчанию (все False)
        self.cheese = False
        self.pepperoni = False
        self.lettuce = False
        self.tomato = False

    def add_cheese(self):
        # Добавление сыра в бургер
        self.cheese = True
        return self

    def add_pepperoni(self):
        # Добавление пепперони в бургер
        self.pepperoni = True
        return self

    def add_lettuce(self):
        # Добавление салата в бургер
        self.lettuce = True
        return self

    def add_tomato(self):
        # Добавление помидора в бургер
        self.tomato = True
        return self

    def build(self):
        # Возвращение экземпляра Burger с текущими ингредиентами
        return Burger(self)

# Создание бургера с ингредиентами
burger = BurgerBuilder().add_pepperoni().add_cheese().build()

# Вывод информации о бургере
burger.display_burger()
