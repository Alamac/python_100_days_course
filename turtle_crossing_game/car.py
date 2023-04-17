from turtle import Turtle
from random import choice, randint

COLORS: str = [
    'red',
    'orange',
    'yellow',
    'green',
    'blue',
    'violet',
    'cyan'
]


class Car(Turtle):

    def __init__(self, speed: int = 3) -> None:
        super().__init__()
        self.color(choice(COLORS))
        self.pu()
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.setpos(300, randint(-260, 260))
        self.setheading(180)
        self.move_speed = speed

    def move(self) -> None:
        self.forward(self.move_speed)

    def delete(self) -> None:
        self.reset()
        self.ht()
        self.pu()
        self.setpos(1000, 1000)
