import turtle

A=turtle.Turtle()

A.getscreen().bgcolor("black")
A.pensize(0)

A.color("white")


def outer_border():
    A.up()
    A.setpos(-90,-150)
    A.down()
    A.begin_fill()
    A.color("white")
    for i in range(2):
        A.forward(230)
        A.circle(60,90)
        A.forward(110)
        A.circle(60,90)
    A.end_fill()

def outer_shape():
    A.up()
    A.setpos(-75,-125)
    A.down()
    A.begin_fill()
    A.color("red")
    for i in range(2):
        A.forward(200)
        A.circle(50,90) 
        A.forward(80)
        A.circle(50,90)
    A.end_fill()

def inner_triangle():
    A.up()
    A.setpos(6,-65)
    A.down()
    A.begin_fill()
    A.color("white")
    A.left(90)
    for i in range(2):
        A.forward(60)
        A.right(120)
    A.forward(60)
    A.end_fill()


outer_border()
outer_shape()
inner_triangle()


A.hideturtle()
turtle.done()