from turtle import Turtle


class Square(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup()


class Circle(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.shape('circle')
        self.color('blue')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
