from random import random

class Rando():

        def random_num(self):
            return ((int)(random() * 10 ))

        def color(self):
            r = self.random_num()

            switcher = {
                0: 'black',
                1: 'white',
                2: 'light grey',
                3: 'dark gray',
                4: 'light brown',
                5: 'dark brown',
                6: 'light orange',
                7: 'dark orange',
                8: 'yellow',
                9: 'cream',
            }

            return switcher.get(r, "black")

        def place(self):
            r = self.random_num()

            switcher = {
                0: 'keyboard',
                1: 'couch',
                2: 'desk',
                3: 'table',
                4: 'lazyboy',
                5: 'porch',
                6: 'sidewalk',
                7: 'floor',
                8: 'shelf',
                9: 'roof',
            }

            return switcher.get(r, "bed")

        def food(self):
            r = self.random_num()

            switcher = {
                0: 'my food',
                1: 'your food',
                2: 'katnip',
                3: 'grass',
                4: 'lazyboy',
                5: 'strawberries',
                6: 'chicken',
                7: 'salmon',
                8: 'potatoes',
                9: 'watermelon',
            }

            return switcher.get(r, "kibbles")