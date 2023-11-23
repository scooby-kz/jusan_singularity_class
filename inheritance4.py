class Fruit:
    def eat(self):
        pass

class Apple(Fruit):
    def eat(self):
        return "Яблоко съедено."

class Pear(Fruit):
    def eat(self):
        return "Груша съедена."

class Orange(Fruit):
    def eat(self):
        return "Апельсин съеден."

# Создаем объекты каждого подкласса
apple = Apple()
pear = Pear()
orange = Orange()

# Вызываем метод eat для каждого объекта
print(apple.eat())
print(pear.eat())
print(orange.eat())