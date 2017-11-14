class Pet(object):

    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print('%s is eating %s.'% (self.name, food))

    def sleep(self):
        print('%s is now curled up and sleeping' % (self.name))

