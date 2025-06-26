import turtle
import random
turtle.colormode(255)

my_turtle=turtle.Turtle()
my_screen=turtle.Screen()

my_turtle.speed(40)
radius=150
turn=0

while turn!=360:
    r,b,g=(random.randint(0,255)for i in range(3))
    col=(r,b,g)
    my_turtle.color(col)
    my_turtle.circle(radius)
    my_turtle.setheading(turn)
    turn+=5













my_screen.exitonclick()