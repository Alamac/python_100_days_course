from turtle import Turtle


class TurtleChar(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.pu()
        self.shape('turtle')
        self.color('black')
        self.setheading(90)
        self.setpos(0, -280)

    def move(self) -> None:
        self.forward(10)

    def reset_position(self) -> None:
        self.setpos(0, -280)
