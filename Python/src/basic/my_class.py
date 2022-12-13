class Animals():
    def breathe(self):
        print('breathing')

    def move(self):
        print('moving')

    def eat(self):
        print("eating food")


class Mammals(Animals):
    def breastfeed(self):
        print("breastfeed")


class Cats(Mammals):
    def __init__(self, spots):
        self.spots = spots

    def catch_mouse(self):
        print("catch mouse")


kitty = Cats(10)
print(kitty.spots)
kitty.eat()
kitty.breastfeed()
