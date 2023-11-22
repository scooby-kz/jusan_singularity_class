class Car():
    def __init__(self, brand='BMW', model=None):
        self.__brand = brand
        self.__module = model


    def get_info(self):
        return (self.__brand, self.__module)

    def change_atr(self, brand, model):
        self.__brand = brand
        if brand.lower() == 'bmw':
            self.__module = model
        else:
            print ('Модель можно менять если это марки BMW')


bmw = Car(model='x5')
print(*bmw.get_info(),sep='\n')

bmw.change_atr('BMW', 'x3')
print("*"*20)
print(*bmw.get_info(),sep='\n')
