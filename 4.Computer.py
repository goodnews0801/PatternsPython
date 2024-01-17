# Класс Computer, представляющий сложную систему
class Computer:
    def start_power_supply(self):
        print("Включение блока питания")

    def start_processor(self):
        print("Включение процессора")

    def start_memory(self):
        print("Включение оперативной памяти")

    def start_hard_drive(self):
        print("Включение жесткого диска")

    def shutdown_power_supply(self):
        print("Отключение блока питания")

    def shutdown_processor(self):
        print("Отключение процессора")

    def shutdown_memory(self):
        print("Отключение оперативной памяти")

    def shutdown_hard_drive(self):
        print("Отключение жесткого диска")

# Фасад для управления компьютером
class ComputerFacade:
    def __init__(self, computer):
        self.computer = computer

    def turn_on(self):
        self.computer.start_power_supply()
        self.computer.start_processor()
        self.computer.start_memory()
        self.computer.start_hard_drive()

    def turn_off(self):
        self.computer.shutdown_hard_drive()
        self.computer.shutdown_memory()
        self.computer.shutdown_processor()
        self.computer.shutdown_power_supply()

# Пример использования
if __name__ == "__main__":
    computer = Computer()
    computer_facade = ComputerFacade(computer)

    # Включаем компьютер через фасад
    computer_facade.turn_on()

    # Выключаем компьютер через фасад
    computer_facade.turn_off()
