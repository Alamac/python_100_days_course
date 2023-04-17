import time
from turtle import Screen, Turtle
from car import Car
from turtle_char import TurtleChar
from level import Level

screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor('white')
screen.title('Turtle Crossing')
screen.tracer(0)

turtle: TurtleChar = TurtleChar()
level: Level = Level()
cars: Car = [Car(3)]


screen.listen()
screen.onkeypress(turtle.move, 'Up')


game_is_on: bool = True
tick: int = 0

while game_is_on:
    tick += 1
    screen.update()
    time.sleep(0.1)
    for c in cars:
        if c.distance(turtle) < 20:
            game_is_on = False
            level.game_over()
            break
        if c.xcor() < -300:
            c.delete()
        c.move()
    if tick % 10 == 0:
        cars.append(Car(level.get_speed()))

    if turtle.ycor() >= 280:
        turtle.reset_position()
        level.increase_level()
        for c in cars:
            c.delete()
        cars.clear()

screen.exitonclick()
