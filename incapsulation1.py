class Bank_account():
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    #Метод для пополнение
    def cash_in(self, money_in):
        self.__balance += money_in
    #Метод для снятия если после останеться более 0 бакса
    def cash_out(self, money_out):
        if self.__balance - money_out < 0:
            print('Не достаточный баланс')
        else:
            self.__balance -= money_out
            print (f"Вы сняли {money_out} со своего счета, остаток {self.__balance}")

MyMoney = Bank_account(7777)
print(MyMoney.get_balance())

MyMoney.cash_out(8000)
print(MyMoney.get_balance())
