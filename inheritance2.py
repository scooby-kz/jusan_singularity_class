class Vehicle:
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        return "Автомобиль едет по дороге."

class Bicycle(Vehicle):
    def move(self):
        return "Велосипед движется по велосипедной дорожке."

class Motorcycle(Vehicle):
    def move(self):
        return "Мотоцикл мчится по шоссе."

# Создаем объекты каждого подкласса
car = Car()
bicycle = Bicycle()
motorcycle = Motorcycle()

# Вызываем метод move для каждого объекта
print(car.move())
print(bicycle.move())
print(motorcycle.move())