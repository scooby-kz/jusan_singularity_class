#Создаем класс Прямоугольник
class Rectangle():
    #задаем атрибуты
    width=0
    height=0
    
    #Creatint method
    def area(self):
        return self.width*self.height


Rectangle1 = Rectangle()
Rectangle1.height=5
Rectangle1.width=4

print(Rectangle1.area())