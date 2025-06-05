class Soda:
    def __init__(self, additive=""):
        self.additive = additive
    
    def show_my_drink(self):
        if self.additive != "":
            print("Газировка и", self.additive)
        else:
            print("Обычная газировка")


cola = Soda("сахар")
cola.show_my_drink()

water = Soda()
water.show_my_drink()