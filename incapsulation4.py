# Создаем класс Книга
class Book():
    def __init__(self, name):
        # Делаем атрубит приватным
        self.__name = name

    # Метод который возвращает название книги
    def get_name(self):
        return self.__name

    # Метод который позволяет задавать имя книги если оно больше 5
    def set_name(self, new_name):
        if len(new_name) > 5:
            self.__name = new_name
            print(f'Было изменено имя книги на {self.__name}')
        else:
            print('Название книги должно быть длинне 5 символов')
# Создаем экземпляр класс (обьект)
HarryPotter = Book('HarryPotter')
# Выводим текущее имя
print(HarryPotter.get_name())
# Пытаемся поменять имя книги в строке 4 буквы
HarryPotter.set_name('Harr')
# Снова пытаем но уже строка длиньше 5 символов
HarryPotter.set_name('HarryPotter2')