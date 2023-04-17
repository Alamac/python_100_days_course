from turtle import Turtle


class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape('circle')
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.color('white')
        self.pu()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self) -> None:
        self.setpos(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def bounce_y(self) -> None:
        self.y_move *= -1

    def bounce_x(self) -> None:
        self.x_move *= -1
        self.move_speed *= 0.9

    def score(self) -> None:
        self.bounce_x()
        self.setpos(0, 0)
        self.reset_speed()

    def reset_speed(self) -> None:
        self.move_speed = 0.1

    def get_speed(self) -> float:
        return self.move_speed
