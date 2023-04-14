from turtle import Turtle, Screen
from random import randint, choice
import colorgram


def get_colors_from_image(image, n):
    raw_colors = colorgram.extract(image, n)
    processed_colors = []
    for c in raw_colors:
        processed_colors.append((c.rgb[0], c.rgb[1], c.rgb[2]))
    return processed_colors


def main():
    colors = get_colors_from_image('image.jpg', 100)
    t = Turtle()
    s = Screen()
    t.speed('fastest')
    t.hideturtle()
    t.pu()
    t.goto(-500, -500)
    s.colormode(255)
    for i in range(10):
        for j in range(10):
            t.dot(20, choice(colors))
            t.forward(50)
        t.left(90)
        t.forward(50)
        t.right(90)
        t.backward(500)

    s.exitonclick()


if __name__ == '__main__':
    main()
