#Создаем класс банк
class bank_account():
    #задаем атрибуты
    id = int
    balance = 0 # Стартовый баланк равен 0

    #Метод для пополнение
    def cash_in(self, money_in):
        self.balance += money_in
    #Метод для снятия
    def cash_out(self, money_out):
        self.balance -= money_out
    #Метод который показывает текущий баланс
    def show_balance(self):
        return self.balance


# Создаем экземпляр класса Банк
my_kaspi = bank_account()
# задаем айди банк счета
my_kaspi.id = 777
# Пополняем баланс
my_kaspi.cash_in(1000)
# Снимаем
my_kaspi.cash_out(300)
# Выводим сумму на балансе
print(my_kaspi.show_balance())
# Result = 700