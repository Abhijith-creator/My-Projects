import turtle
turtle.colormode(255)
from  random import *

my_turtle=turtle.Turtle()
my_screen=turtle.Screen()

#Function for random color
# def random_col():
#     r=randint(0, 255)
#     g= randint(0, 255)
#     b= randint(0, 255)
#     col=(r, g, b)
#     return col


path=[0, 90, 180, 270]
my_turtle.speed(50)
my_turtle.pensize(10)


for _ in range(100):
    r, g, b = (randint(0, 255) for _ in range(3))
    my_turtle.color(r,g,b)
    my_turtle.setheading(choice(path))
    my_turtle.forward(30)


my_screen.exitonclick()
