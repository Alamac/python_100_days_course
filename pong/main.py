import time
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

def draw_line():
    line = Turtle()
    line.speed('fastest')
    line.ht()
    line.setpos(0, 300)
    line.setheading(270)
    line.pencolor('white')
    line.pensize(3)
    line.shape('square')
    while line.ycor() >= -300:
        line.forward(10)
        line.pu()
        line.forward(10)
        line.pd()


screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)
draw_line()


l_paddle = Paddle('left')
r_paddle = Paddle('right')
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(l_paddle.up, 'w')
screen.onkeypress(l_paddle.down, 's')
screen.onkeypress(r_paddle.up, 'Up')
screen.onkeypress(r_paddle.down, 'Down')

game_is_on = True
while game_is_on:
    time.sleep(ball.get_speed())
    scoreboard.update()
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if (ball.xcor() > 330 and ball.distance(r_paddle) < 50) or (ball.xcor() < -330 and ball.distance(l_paddle) < 50):
        ball.bounce_x()

    if ball.xcor() > 400:
        ball.score()
        scoreboard.l_score += 1

    if ball.xcor() < -400:
        ball.score()
        scoreboard.r_score += 1

screen.exitonclick()
