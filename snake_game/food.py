from shape import Circle
from random import randint


class Food(Circle):

    def __init__(self):
        super().__init__()
        self.speed('fastest')
        self.reposition()

    def reposition(self):
        random_x = randint(-280, 280)
        random_x = random_x - random_x % 20
        random_y = randint(-280, 280)
        random_y = random_y - random_y % 20
        self.goto(random_x, random_y)
