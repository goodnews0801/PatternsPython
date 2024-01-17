from typing import List

# Интерфейс для посредника
class ChatMediator:
    def send_message(self, user, message):
        pass

# Класс пользователя чата
class ChatUser:
    def __init__(self, name, mediator):
        self.name = name
        self.mediator = mediator

    def send_message(self, message):
        print(f"{self.name} отправляет сообщение: {message}")
        self.mediator.send_message(self, message)

    def receive_message(self, message):
        print(f"{self.name} получает сообщение: {message}")

# Реализация посредника для чата
class ChatMediatorImpl(ChatMediator):
    def __init__(self):
        self.users: List[ChatUser] = []

    def add_user(self, user):
        self.users.append(user)

    def send_message(self, user, message):
        for u in self.users:
            if u != user:  # не отправлять сообщение отправителю
                u.receive_message(message)

# Пример использования
if __name__ == "__main__":
    mediator = ChatMediatorImpl()

    user1 = ChatUser("User1", mediator)
    user2 = ChatUser("User2", mediator)
    user3 = ChatUser("User3", mediator)

    mediator.add_user(user1)
    mediator.add_user(user2)
    mediator.add_user(user3)

    user1.send_message("Привет, как дела?")
    user2.send_message("Привет! Всё отлично, спасибо!")
    user3.send_message("Привет, ребята!")


