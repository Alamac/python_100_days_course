from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, side) -> None:
        super().__init__()
        self.shape('square')
        self.color('white')
        self.pu()
        self.shapesize(stretch_wid=5, stretch_len=1)
        if side == 'left':
            self.setpos(-350, 0)
        if side == 'right':
            self.setpos(350, 0)

    def up(self) -> None:
        if self.ycor() < 240:
            self.goto(self.xcor(), self.ycor() + 20)

    def down(self) -> None:
        if self.ycor() > -240:
            self.goto(self.xcor(), self.ycor() - 20)
