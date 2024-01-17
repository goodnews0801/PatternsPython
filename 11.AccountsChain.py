from abc import ABC, abstractmethod

# Интерфейс обработчика
class PaymentHandler(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

# Конкретный обработчик для банковской карты
class CreditCardHandler(PaymentHandler):
    def process_payment(self, amount):
        if amount <= self.available_balance:
            print("Оплата банковской картой")
        elif self.next_handler:
            self.next_handler.process_payment(amount)

# Конкретный обработчик для Paypal
class PaypalHandler(PaymentHandler):
    def process_payment(self, amount):
        if amount <= self.available_balance:
            print("Оплата Paypal")
        elif self.next_handler:
            self.next_handler.process_payment(amount)

# Конкретный обработчик для Bitcoin кошелька
class BitcoinHandler(PaymentHandler):
    def process_payment(self, amount):
        if amount <= self.available_balance:
            print("Оплата Bitcoin кошельком")
        elif self.next_handler:
            self.next_handler.process_payment(amount)

# Класс цепочки ответственности
class PaymentChain:
    def __init__(self):
        self.handlers = []

    def add_handler(self, handler):
        if self.handlers:
            self.handlers[-1].next_handler = handler
        self.handlers.append(handler)

    def process_payment(self, amount):
        if self.handlers:
            self.handlers[0].process_payment(amount)

# Пример использования
if __name__ == "__main__":
    payment_chain = PaymentChain()

    # Создаем обработчики счетов с указанием приоритета
    credit_card_handler = CreditCardHandler()
    paypal_handler = PaypalHandler()
    bitcoin_handler = BitcoinHandler()

    # Добавляем обработчики в цепочку
    payment_chain.add_handler(credit_card_handler)
    payment_chain.add_handler(paypal_handler)
    payment_chain.add_handler(bitcoin_handler)

    # Устанавливаем доступные средства на каждом аккаунте
    credit_card_handler.available_balance = 500
    paypal_handler.available_balance = 200
    bitcoin_handler.available_balance = 100

    # Пытаемся оплатить счет с заданным объемом
    payment_chain.process_payment(300)
