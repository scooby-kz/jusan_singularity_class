class Shape:
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        return "Круг нарисован."

class Square(Shape):
    def draw(self):
        return "Квадрат нарисован."

class Triangle(Shape):
    def draw(self):
        return "Треугольник нарисован."

# Создаем объекты каждого подкласса
circle = Circle()
square = Square()
triangle = Triangle()

# Вызываем метод draw для каждого объекта
print(circle.draw())
print(square.draw())
print(triangle.draw())