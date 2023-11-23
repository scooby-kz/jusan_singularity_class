class animal():
    def make_sound(self):
        pass

class dog(animal):
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print ("Собака гафкает")

sharik = dog('sharik')
sharik.make_sound()


class cat(animal):
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print (f"{self.name} мяукает")

Tika = cat('Tika')
Tika.make_sound()

class leo(animal):
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print ("лев рычит")

leo = leo('Tika')
leo.make_sound()