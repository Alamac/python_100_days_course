from shape import Square

MOVE_DISTANCE = 20
DIRECTION = {
    "RIGHT": 0,
    "UP": 90,
    "LEFT": 180,
    "DOWN": 270
}


class Snake:

    def __init__(self, size: int) -> None:
        self.size = size
        self.snake = []
        for i in range(size):
            t = Square()
            t.setx(i * -20)
            self.snake.append(t)
        self.head = self.snake[0]

    def left(self) -> None:
        if self.snake[0].heading() != DIRECTION["RIGHT"]:
            self.snake[0].setheading(DIRECTION["LEFT"])

    def right(self) -> None:
        if self.snake[0].heading() != DIRECTION["LEFT"]:
            self.snake[0].setheading(DIRECTION["RIGHT"])

    def down(self) -> None:
        if self.snake[0].heading() != DIRECTION["UP"]:
            self.snake[0].setheading(DIRECTION["DOWN"])

    def up(self) -> None:
        if self.snake[0].heading() != DIRECTION["DOWN"]:
            self.snake[0].setheading(DIRECTION["UP"])

    def move(self) -> None:
        for i in range(self.size - 1, 0, -1):
            self.snake[i].goto(self.snake[i - 1].pos())
        self.snake[0].forward(MOVE_DISTANCE)

    def grow(self) -> None:
        last_pos = self.snake[-1].pos()
        t: Square = Square()
        t.setpos(last_pos)
        self.snake.append(t)
        self.size += 1

    def check_self_collision(self) -> bool:
        for i in self.snake[1:]:
            if self.head.distance(i) < 10:
                return True
        return False

    def check_wall_collision(self) -> bool:
        x_cor = self.head.xcor()
        y_cor = self.head.ycor()
        return x_cor >= 300 or x_cor <= -300 or y_cor >= 300 or y_cor <= -300

    def reset(self) -> None:
        for s in self.snake:
            s.ht()
            s.setpos(3000, 3000)
        self.snake.clear()
        self.__init__(3)
