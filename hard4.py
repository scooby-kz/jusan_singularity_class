class Bank:
    def __init__(self):
        self.clients = []

    def open_account(self, client_name, initial_balance=0):
        if not self._find_client(client_name):
            new_client = Client(client_name, initial_balance)
            self.clients.append(new_client)
            print(f'Открыт новый банковский счет для клиента {client_name}.')
        else:
            print(f'Клиент {client_name} уже имеет банковский счет.')

    def close_account(self, client_name):
        client = self._find_client(client_name)
        if client:
            self.clients.remove(client)
            print(f'Банковский счет для клиента {client_name} закрыт.')
        else:
            print(f'Клиент {client_name} не найден. Закрытие счета невозможно.')

    def transfer_money(self, sender_name, receiver_name, amount):
        sender = self._find_client(sender_name)
        receiver = self._find_client(receiver_name)

        if sender and receiver:
            if sender.balance >= amount:
                sender.withdraw(amount)
                receiver.deposit(amount)
                print(f'Перевод {amount} руб. счета клиента {sender_name} на счет клиента {receiver_name} выполнен успешно.')
            else:
                print(f'Недостаточно средств на счете клиента {sender_name} для выполнения перевода.')
        else:
            print('Один из клиентов не найден. Перевод невозможен.')

    def _find_client(self, client_name):
        for client in self.clients:
            if client.name == client_name:
                return client
        return None

class Client:
    def __init__(self, name, initial_balance):
        self.name = name
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

# Пример использования:

# Создаем объект банка
bank = Bank()

# Открываем банковские счета для клиентов
bank.open_account("Alice", initial_balance=1000)
bank.open_account("Bob", initial_balance=500)

# Переводим деньги между счетами
bank.transfer_money("Alice", "Bob", amount=200)

# Закрываем банковский счет
bank.close_account("Alice")