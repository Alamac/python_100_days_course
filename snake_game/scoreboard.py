from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Arial', 18, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.ht()
        self.setpos(0, 270)
        self.color('white')
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.setpos(0, 0)
        self.write(f"Game over.", align=ALIGNMENT, font=FONT)
