import turtle

A=turtle.Turtle()
A.getscreen().bgcolor("black")

A.pensize(5)
A.pencolor("white")
A.up()
A.setpos(20,50)
A.down()

#apple logo
A.begin_fill()
A.color("white")
A.left(160)
A.circle(100,100)
A.circle(200,60)
A.circle(40,90)
A.circle(-40,100)
A.circle(40,100)
A.circle(200,30)
A.left(90)
A.circle(-70,150)
A.left(120)
A.circle(160,55)
A.end_fill()


A.up()
A.setpos(20,65)
A.down()
A.begin_fill()
A.color("white")
A.rt(175)
A.circle(140,50)
A.lt(130)
A.circle(140,50)
A.end_fill()





A.hideturtle()
turtle.done()