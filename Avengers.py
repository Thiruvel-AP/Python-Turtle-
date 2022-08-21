import turtle

A=turtle.Turtle()
A.speed(5)
A.pensize(10)
A.pencolor("white")

A.getscreen().bgcolor("black")
A.color("white")

def circle():
    A.begin_fill()
    A.up()
    A.setpos(0,-280)
    A.down()
    A.circle(300)
    A.color("red")
    A.end_fill()
    
    

def innercircle():
    A.up()
    A.setpos(0,-230)
    A.down()
    A.speed(15)
    A.pensize(2)
    A.begin_fill()
    A.circle(250)
    A.color("black")
    A.end_fill()
    

def draw_A():
    A.up()
    A.setpos(30,-110)
    A.speed(5)
    A.begin_fill()
    A.down()
    A.color("white","red")
    A.pensize(10)
    A.forward(23)
    A.backward(123)
    A.left(60)
    A.backward(220)
    A.right(60)
    A.backward(100)
    A.left(60)
    A.forward(740)
    A.right(60)
    A.forward(60)
    A.right(90)
    A.forward(500)
    A.left(90)
    A.backward(75)
    A.left(110)
    A.forward(52)
    A.end_fill()
    

def triangle():
    A.up()
    A.setpos(53,-40)
    A.begin_fill()
    A.down()
    A.color("white","black")
    A.left(70)
    A.forward(80)
    A.right(120)
    A.forward(150)
    A.left(35)
    A.backward(130)
    A.end_fill()
    


def arrow():
    A.up()
    A.down()
    A.forward(68)
    A.right(140)
    A.forward(122)
    A.right(78)
    A.forward(118)

    
    

circle()
innercircle()
draw_A()
triangle()
arrow()


A.hideturtle()
turtle.done()
