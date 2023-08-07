
from turtle import *
from random import randint
speed(0)
colormode(255)
up()
for i in range(2000):
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    x = randint(-240, 240)
    y = randint(-180, 180)
    goto(x, y)
    dot(randint(1, 20), (r, g, b))
hideturtle()