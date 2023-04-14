import time
from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake')
screen.tracer(0)

snake = Snake(3)
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")

game_is_on = True
while game_is_on:
    screen.update()
    snake.move()
    time.sleep(0.1)

    if snake.head.distance(food) < 10:
        food.reposition()
        snake.grow()
        scoreboard.increase_score()

    if snake.check_self_collision():
        game_is_on = False

    if snake.head.xcor() >= 300 or snake.head.xcor() <= -300 or snake.head.ycor() >= 300 or snake.head.ycor() <= -300:
        game_is_on = False

scoreboard.game_over()

screen.exitonclick()
