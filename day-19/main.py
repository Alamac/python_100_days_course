from turtle import Turtle, Screen
from random import randint


def goto_start_position(turtle, offset=0, number_of_participants=6):
    turtle.penup()
    turtle.goto(x=-240, y=number_of_participants / 2 * 20 - offset)


def move_forward(turtle):
    turtle.forward(randint(1, 10))


def is_winner(turtle):
    if turtle.xcor() >= 250:
        return True
    return False


turtles = {
    'red': Turtle(shape='turtle'),
    'orange': Turtle(shape='turtle'),
    'yellow': Turtle(shape='turtle'),
    'green': Turtle(shape='turtle'),
    'blue': Turtle(shape='turtle'),
    'violet': Turtle(shape='turtle'),
    'cyan': Turtle(shape='turtle')
}

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet: ", prompt="Enter the color of the winner: ").lower()
for key, value in turtles.items():
    value.color(key)
for i in range(len(turtles)):
    goto_start_position(turtle=list(turtles.values())[i], offset=i * 20, number_of_participants=len(turtles))

winner = ''
while winner == '':
    for color, t in turtles.items():
        move_forward(t)
        if is_winner(t):
            winner = color
            break
screen.bye()

if user_bet == winner:
    print(f'You got it right! The winner is {winner}')
else:
    print(f'You got it wrong! The winner is {winner}')
