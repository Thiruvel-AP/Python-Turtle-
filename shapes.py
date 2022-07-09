import turtle

A=turtle.Turtle()
A.speed(20)

A.getscreen().bgcolor("black")
A.color("black")

A.color("white")

color=["cyan","hotpink","gold","purple","red","blue","indigo"]

A.up()
A.setpos(-25,150)
A.down()

def shape(color):
    for i in range(6):
        A.speed(20)
        A.begin_fill()
        A.pencolor(color[i%2])
        A.forward(15)
        A.left(60)  
        A.end_fill()
           
def move():
    for i in range(6):
        shape(color)
        A.left(60)
        A.forward(80)
        
def repeat():
    for i in range(6):
        move()
        A.left(60)
        A.forward(120)

def shaperepeat():
    for i in range(6):
        repeat()
        A.right(60)
        A.forward(180)
        
        
           


shaperepeat()





A.hideturtle()
turtle.done()
