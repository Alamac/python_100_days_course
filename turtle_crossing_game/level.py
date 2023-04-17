from turtle import Turtle

BASE_SPEED = 3
FONT = ('Courier', 20, 'normal')

class Level(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.pu()
        self.ht()
        self.color('black')
        self.level = 1
        self.level_speed = BASE_SPEED
        self.setpos(-300, 270)
        self.update()

    def update(self) -> None:
        self.clear()
        self.write(f'Level: {self.level}', align='left', font=FONT)

    def increase_level(self) -> None:
        self.clear()
        self.level += 1
        self.level_speed = BASE_SPEED * self.level
        self.update()

    def get_speed(self) -> int:
        return self.level_speed


    def game_over(self):
        self.clear()
        self.setpos(0, 0)
        self.write('Game Over', align='center', font=FONT)
