import re

# Creating class Phone
class Phone():
    def __init__(self, phone_number):
        # athribute phone_number is private
        self.__phone_number = phone_number

    # method that show number
    def show_number(self):
        return self.__phone_number

    # method that changes number
    def change_number(self, phone_number):
        print (re.search(f'7-\d{3}-\d{5}', phone_number))
        # С помощью регулярки проверяем корректность номера
        if re.search('7-\d{3}-\d{5}', phone_number):
            self.__phone_number = phone_number
        else:
            print('Номер не являеться корректным телефонным номером')

# Создаем обьект на основке класса Phone с начальным номером 0-000-00000
Myphone = Phone('7-000-00000')
print(Myphone.show_number())

Myphone.change_number('123456')
print(Myphone.show_number())

Myphone.change_number('7-777-12345')
print(Myphone.show_number())

