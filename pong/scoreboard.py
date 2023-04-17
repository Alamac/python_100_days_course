from turtle import Turtle

ALIGN = 'center'
FONT = ('Courier', 50, 'normal')


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.color('white')
        self.pu()
        self.ht()
        self.l_score = 0
        self.r_score = 0
        self.update()

    def update(self) -> None:
        self.clear()
        self.setpos(-50, 220)
        self.write(self.l_score, align=ALIGN, font=FONT)
        self.setpos(50, 220)
        self.write(self.r_score, align=ALIGN, font=FONT)