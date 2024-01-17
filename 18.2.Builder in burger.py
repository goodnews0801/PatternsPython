class Burger:
    def __init__(self, cheese=False, pepperoni=False, lettuce=False, tomato=False):
        # Инициализация бургера с ингредиентами
        self.cheese = cheese
        self.pepperoni = pepperoni
        self.lettuce = lettuce
        self.tomato = tomato

    # Вложенный класс Builder, отвечающий за пошаговое строение бургера
    class Builder:
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
            return Burger(self.cheese, self.pepperoni, self.lettuce, self.tomato)

# Создание бургеров пошагово
burger1 = Burger.Builder().add_pepperoni().add_cheese().build()
burger2 = Burger.Builder().add_lettuce().add_tomato().build()

# Вывод информации о бургерах
print(f"Burger 1: Cheese - {burger1.cheese}, Pepperoni - {burger1.pepperoni}")
print(f"Burger 2: Lettuce - {burger2.lettuce}, Tomato - {burger2.tomato}")
