class Student():
    name = str
    age = int
    average = float


    def is_good(self):
        if self.average > 4.5:
            print (f'{self.name} is good student (average) is more than 4.5')
        elif self.average < 4.5:
            print (f'{self.name} is bad student (average) is less than 4.5')
         


tom = Student()
tom.name = "Tom"
tom.age = 20
tom.average = 4.3
tom.is_good()

jerry = Student()
jerry.name = "Jerry"
jerry.age = 21
jerry.average = 4.9
jerry.is_good()