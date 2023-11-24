# Создаем класс
class shop():
    inventory = []
    # Метод по добавлению
    def add_to_inventory(self, item):
        self.inventory.append(item)
    # МЕтод по удалению
    def del_fr_inventory(self, item):
        self.inventory.remove(item)
    # Показать инвентарь
    def show_inventory(self):
        return self.inventory



myshow = shop()
# Добавляем товар
myshow.add_to_inventory('Pivo')
print(*myshow.show_inventory())
# Удаляем товар
myshow.del_fr_inventory('Pivo')
print(*myshow.show_inventory())