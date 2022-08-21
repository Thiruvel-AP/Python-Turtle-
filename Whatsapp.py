import turtle

A=turtle.Turtle()
A.getscreen().bgcolor("black")

# A.width(0.35)

# A.pencolor("white")
# whatsapp logo
# inner portion
A.width(15)
A.begin_fill()
A.color("white","green")
A.speed(5)
A.up()
A.setpos(-150,-120)
A.down()
A.lt(30)
A.fd(60)
A.rt(70)
A.circle(180,345)
A.rt(52)
A.fd(67)
A.end_fill()

# inner call 
A.width(3)
A.pencolor("white")
A.begin_fill()
A.color("white")
A.speed(5)
A.up()
A.setpos(-100,130)
A.down()
A.lt(30)
A.circle(250,70)
A.lt(50)
A.circle(30,170)
A.rt(50)
A.circle(-200,50)
A.rt(50)
A.circle(30,170)
A.end_fill()










A.hideturtle()
turtle.done()
