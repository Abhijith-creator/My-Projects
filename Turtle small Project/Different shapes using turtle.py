from turtle import Turtle,Screen
import  random

my_turtle=Turtle()
my_screen=Screen()
colors = [
    'red',
    'blue',
    'green',
    'orange',
    'purple',
    'cyan',
    'magenta',
    'yellow',
    'navy',
    'teal',
    'olive'
]



def next_scape(si):
    ang=360/si
    for _ in range(si):
        my_turtle.forward(100)
        my_turtle.right(ang)


for side in range(3,7):
    my_turtle.color(random.choice(colors))
    next_scape(side)

my_screen.exitonclick()
