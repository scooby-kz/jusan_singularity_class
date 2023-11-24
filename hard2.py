# Создаем класс Задачи
class Task():
    # Задаем базовые параметры
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
        self.statuses = ["done","in progress", "not yet"]
        self.status = None

    # Метод который меняет статус
    def change_status(self, code_of_status):
        self.status = self.statuses[code_of_status]
    # Метод который показывает текущий статут
    def show_status(self):
        return self.status
# Создаем экземпляр класса
first = Task('first', "my fisrt task", )
print(first.show_status())
# Меняем статус
first.change_status(0)
# Выводим текущий статус
print(first.show_status())