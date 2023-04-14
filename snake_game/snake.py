from shape import Square

MOVE_DISTANCE = 20
DIRECTION = {
    "RIGHT": 0,
    "UP": 90,
    "LEFT": 180,
    "DOWN": 270
}


class Snake:

    def __init__(self, size):
        self.size = size
        self.snake = []
        for i in range(size):
            t = Square()
            t.setx(i * -20)
            self.snake.append(t)
        self.head = self.snake[0]

    def add_segment(self):
        pass

    def left(self):
        if self.snake[0].heading() != DIRECTION["RIGHT"]:
            self.snake[0].setheading(DIRECTION["LEFT"])

    def right(self):
        if self.snake[0].heading() != DIRECTION["LEFT"]:
            self.snake[0].setheading(DIRECTION["RIGHT"])

    def down(self):
        if self.snake[0].heading() != DIRECTION["UP"]:
            self.snake[0].setheading(DIRECTION["DOWN"])

    def up(self):
        if self.snake[0].heading() != DIRECTION["DOWN"]:
            self.snake[0].setheading(DIRECTION["UP"])

    def move(self):
        for i in range(self.size - 1, 0, -1):
            self.snake[i].goto(self.snake[i - 1].pos())
        self.snake[0].forward(MOVE_DISTANCE)

    def grow(self):
        last_pos = self.snake[-1].pos()
        t = Square()
        t.setpos(last_pos)
        self.snake.append(t)
        self.size += 1

    def check_self_collision(self):
        for i in self.snake[1:]:
            if self.head.distance(i) < 10:
                return True
        return False
