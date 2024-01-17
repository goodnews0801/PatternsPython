# Интерфейс двери
class Door:
    def open_door(self):
        pass

    def close_door(self):
        pass

# Реализация обычной двери
class SimpleDoor(Door):
    def open_door(self):
        print("Дверь открыта")

    def close_door(self):
        print("Дверь закрыта")

# Прокси с защитой паролем
class PasswordProtectedDoorProxy(Door):
    def __init__(self, real_door, password):
        self.real_door = real_door
        self.password = password

    def open_door(self):
        if self.authenticate():
            self.real_door.open_door()
        else:
            print("Неверный пароль. Дверь не открывается.")

    def close_door(self):
        if self.authenticate():
            self.real_door.close_door()
        else:
            print("Неверный пароль. Дверь не закрывается.")

    def authenticate(self):
        # Здесь может быть ваша логика проверки пароля
        return input("Введите пароль: ") == self.password

# Пример использования
if __name__ == "__main__":
    simple_door = SimpleDoor()

    # Создаем прокси с защитой паролем, передавая ему реальную дверь и пароль
    password_protected_door_proxy = PasswordProtectedDoorProxy(simple_door, "ваш_пароль")

    # Попытка открытия двери через прокси
    password_protected_door_proxy.open_door()

    # Попытка закрытия двери через прокси
    password_protected_door_proxy.close_door()
