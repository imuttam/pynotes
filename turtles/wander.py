import turtle
a = turtle.Turtle()
a.shape('turtle')
a.shapesize(2,2,2)

colors = ['red','blue','orange','green','purple','pink','yellow']
a.pensize(10 )

import random

x = 200

while True:
    a.color(random.choice(colors))
    a.fd(random.randint(90,400))
    a.lt(random.randint(90,95))
    if a.xcor() > x or a.xcor() > -x or a.ycor() > x or a.ycor() > -x :
        a.lt(120)