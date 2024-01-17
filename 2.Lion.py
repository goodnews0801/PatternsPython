# Определяем интерфейс Lion
class Lion:
    def roar(self):
        pass

# Реализация класса AfricanLion, наследующего интерфейс Lion
class AfricanLion(Lion):
    def roar(self):
        print("Африканский лев сказал Ррррррр")

# Реализация класса AsianLion, также наследующего интерфейс Lion
class AsianLion(Lion):
    def roar(self):
        print("Азиатский лев сказал Ррррррр")

# Класс WildDog, имеющий метод bark()
class WildDog:
    def bark(self):
        print("Дикая собака сказала Гав-гав")

# Адаптер для WildDog, реализующий интерфейс Lion
class WildDogAdapter(Lion):
    def __init__(self, wild_dog):
        self.wild_dog = wild_dog

    def roar(self):
        self.wild_dog.bark()

# Класс Hero охотится на объекты, реализующие интерфейс Lion
class Hero:
    def find(self, lion):
        print("Герой увидел зверя")
        lion.roar()

# Пример использования
if __name__ == "__main__":
    african_lion = AfricanLion()
    asian_lion = AsianLion()
    wild_dog = WildDog()

    # Создаем адаптер для WildDog
    wild_dog_adapter = WildDogAdapter(wild_dog)

    hero = Hero()

    hero.find(african_lion)
    hero.find(asian_lion)
    hero.find(wild_dog_adapter)  # Теперь герой может охотиться на дикую собаку через адаптер
