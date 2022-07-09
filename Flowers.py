import turtle
A=turtle.Turtle()
A.speed(50)

A.getscreen().bgcolor("black")

color=["hotpink","cyan","gold","skyblue","violet","green","indigo","red"]


def drawshape(angle):
    for i in range(75):
        A.pencolor(color[i%4])
        A.forward(200)
        A.left(angle)

def move():
    for i in range(12):
        A.forward(400)
        A.left(45)
        drawshape(175)

def position():
    for i in range(2):
        move()
        A.up()
        A.goto(-600,0)
        A.forward(1)
        A.down()
        
position()

A.hideturtle()

turtle.done()