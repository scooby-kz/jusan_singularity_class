class Car():
    brand = str
    model = str
    date = int

    def info(self):
        return f'brand:{self.brand}\nmodel:{self.model}\ndate:{self.date}'


bmw = Car()

bmw.brand = 'BMW'
bmw.model = 'x5'
bmw.date = 2010


print(bmw.info())