from turtle import Turtle
import os

ALIGNMENT = 'center'
FONT = ('Arial', 18, 'normal')


class Scoreboard(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.high_score = self.read_highscore_from_file('highscore') or 0
        self.ht()
        self.setpos(0, 270)
        self.color('white')
        self.update_scoreboard()

    def update_scoreboard(self) -> None:
        self.clear()
        self.write(f"Score: {self.score} Highscore: {self.high_score}", align=ALIGNMENT, font=FONT)

    def read_highscore_from_file(self, file='highscore') -> int:
        if os.path.isfile(file):
            with open(file, 'r') as f:
                return int(f.readline())
        return 0

    def write_highscore_to_file(self, file='highscore'):
        with open(file, 'w') as f:
            f.write(str(self.high_score))

    def increase_score(self) -> None:
        self.score += 1
        self.update_scoreboard()

    def game_over(self) -> None:
        self.setpos(0, 0)
        self.write(f"Game over.", align=ALIGNMENT, font=FONT)

    def reset(self) -> None:
        if self.score > self.high_score:
            self.high_score = self.score
        self.write_highscore_to_file()
        self.score = 0
        self.update_scoreboard()
