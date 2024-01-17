# Интерфейс файла
class File:
    def read(self, name):
        pass

# Реализация простого файла
class SimpleFile(File):
    def read(self, name):
        print(f"Читаем файл {name}")

# Прокси с защитой
class ProtectedFileProxy(File):
    def __init__(self, real_file, password):
        self.real_file = real_file
        self.password = password

    def read(self, name):
        if self.check_password():
            self.real_file.read(name)
        else:
            print("Неверный пароль. Доступ запрещен.")

    def check_password(self):
        # Здесь может быть ваша логика проверки пароля
        return self.password == ""

# Пример использования
if __name__ == "__main__":
    simple_file = SimpleFile()

    # Создаем прокси с защитой, передавая ему реальный файл и пароль
    protected_file_proxy = ProtectedFileProxy(simple_file, "123")

    # Попытка чтения файла через прокси
    protected_file_proxy.read("ImportantInfo")
