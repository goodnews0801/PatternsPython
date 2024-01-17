from abc import ABC, abstractmethod

# Интерфейс обработчика
class Handler(ABC):
    @abstractmethod
    def handle_request(self, headers):
        pass

# Конкретный обработчик для добавления заголовка User-Agent
class UserAgentHandler(Handler):
    def handle_request(self, headers):
        headers['User-Agent'] = 'Mozilla/5.0'

# Конкретный обработчик для добавления заголовка Accept-Language
class AcceptLanguageHandler(Handler):
    def handle_request(self, headers):
        headers['Accept-Language'] = 'en-US,en;q=0.9'

# Конкретный обработчик для добавления других заголовков (по желанию)
class OtherHeadersHandler(Handler):
    def handle_request(self, headers):
        # Добавление других заголовков по необходимости
        pass

# Класс цепочки ответственности
class HeadersChain:
    def __init__(self):
        self.handlers = []

    def add_handler(self, handler):
        self.handlers.append(handler)

    def process_request(self, headers):
        for handler in self.handlers:
            handler.handle_request(headers)

# Пример использования
if __name__ == "__main__":
    headers_chain = HeadersChain()

    # Добавляем обработчики в цепочку
    headers_chain.add_handler(UserAgentHandler())
    headers_chain.add_handler(AcceptLanguageHandler())
    headers_chain.add_handler(OtherHeadersHandler())  # Добавьте другие обработчики по необходимости

    # Создаем заголовки и обрабатываем запрос
    request_headers = {}
    headers_chain.process_request(request_headers)

    # Выводим результат
    print(request_headers)
