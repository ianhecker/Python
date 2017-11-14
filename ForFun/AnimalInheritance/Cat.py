from AnimalInheritance.Pet import Pet
from AnimalInheritance.Rando import Rando

class Cat(Pet):

    def __init__(self, name):
        r = Rando()
        self.r = r

        super(Cat, self).__init__(name)
        self.color = r.color()

    def sun_bathe(self, place):
        print('%s sunbathes on the %s' % (self.name, place))

    def shed(self):
        print('%s sheds %s colored fur everywhere!'  % (self.name, self.color))

    def daily_routine(self):

        super().eat(self.r.food())
        self.shed()
        self.sun_bathe(self.r.place())
        super().sleep()

        print('')


