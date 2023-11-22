# Создаем класс студент, где все атрибуты являються приватными
class Student():
    def __init__(self, name, age, average_score):
        self.__name = name
        self.__age = age
        # Добавляем проверку на то чтобы average_score должен быть между 0 и 5
        if 0 < average_score < 5:
            self.__average_score = average_score
        else:
            print('average_score должен быть в диапозоне от 0 до 5')
            exit()

    # Создаем метод который выводит инфу про студента
    def get_info(self):
        return f'name: {self.__name}\nage: {self.__age}\nscore: {self.__average_score}'

# Проверяем
Tom = Student("Tom", 22, 3)
print(Tom.get_info())
print("*"*30)
Jerry = Student("Jerry", 22, 7)
print(Jerry.get_info())