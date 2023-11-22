class Figure():       
    def square(self):
        pass


class Kvadrat(Figure):
    def __init__(self, side) -> None:
        super().__init__()
        self.side = side

    def square(self,side):
        return side**2


class Rectangle(Figure):
    def __init__(self, shirina, visota) -> None:
        super().__init__()
        self.shirina = shirina
        self.visota = visota

    def square(self,shirina,visota):
        return visota*shirina


class triangle(Figure):
    def __init__(self, visota, osnova) -> None:
        super().__init__()
        self.visota = visota
        self.osnova = osnova

    def square(self,visota, osnova):
        return 2*visota*0.5*osnova


kv = Kvadrat(2)
print(f'площадь квадрата = {kv.square(kv.side)}')

rc = Rectangle(2,4)
print(f'площадь прямоугольника = {rc.square(rc.shirina, rc.visota)}')

tr = triangle(2,4)
print(f'площадь треугольника = {tr.square(tr.visota, tr.osnova)}')
