import turtle
A=turtle.Turtle()

A.getscreen().bgcolor("black")
A.color("white")

A.pensize(7.5)


color=["#8a3ab9","#e95950","#bc2a8d","#fccc63"]

def outer_border():
    A.up()
    A.setpos(-120,-288)
    A.down()
    A.begin_fill()
    A.color("white")
    for i in range(4):
        A.forward(240)
        A.circle(60,90)
    A.end_fill()



def outer_shape():
        A.up()
        A.setpos(-100,-260)
        A.down()
        A.pensize(22)
        A.begin_fill()
        A.color("#EA21AD")
        A.fillcolor("white")
        for i in range(4):
            A.forward(200)
            A.circle(50,90)
        A.end_fill() 
    
def inner_circle():
    A.up()
    A.setpos(2.5,-207)
    A.down()
    A.pensize(22)
    A.color("#EA21AD")
    A.circle(95)


def small_circle():
    A.begin_fill()
    A.color("#EA21AD")
    A.up()
    A.setpos(108,-20)
    A.down()
    A.circle(10)
    A.end_fill()



outer_border()
outer_shape()
inner_circle()
small_circle()







A.hideturtle()

turtle.done()