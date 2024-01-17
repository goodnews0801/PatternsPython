# Интерфейс команды заказа
class OrderCommand:
    def execute(self):
        pass

# Команда создания заказа
class OrderAddCommand(OrderCommand):
    def __init__(self, order_id):
        self.order_id = order_id

    def execute(self):
        print(f"Adding order: {self.order_id}")

# Команда оплаты заказа
class OrderPayCommand(OrderCommand):
    def __init__(self, order_id):
        self.order_id = order_id

    def execute(self):
        print(f"Paying order: {self.order_id}")

# Команда отмены заказа
class OrderCancelCommand(OrderCommand):
    def __init__(self, order_id):
        self.order_id = order_id

    def execute(self):
        print(f"Cancel order: {self.order_id}")

# Класс управления заказами
class OrderManager:
    def __init__(self):
        self.commands = []

    def add_command(self, command):
        self.commands.append(command)

    def process_commands(self):
        for command in self.commands:
            command.execute()

    def clear_commands(self):
        self.commands = []

# Пример использования
if __name__ == "__main__":
    order_manager = OrderManager()

    # Создаем команды для заказов
    add_command1 = OrderAddCommand(1)
    pay_command1 = OrderPayCommand(1)
    cancel_command1 = OrderCancelCommand(1)

    add_command2 = OrderAddCommand(2)
    pay_command2 = OrderPayCommand(2)

    # Добавляем команды в менеджер заказов
    order_manager.add_command(add_command1)
    order_manager.add_command(pay_command1)
    order_manager.add_command(cancel_command1)

    order_manager.add_command(add_command2)
    order_manager.add_command(pay_command2)

    # Обработка команд
    order_manager.process_commands()

    # Очищаем команды
    order_manager.clear_commands()
