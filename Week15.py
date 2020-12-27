import turtle 
shelly = turtle.Turtle() 
shelly.shape("turtle")
shelly.position()

shelly.color("red", "yellow") 

shelly.pencolor("black")

shelly.turtlesize(7,9,2) 
shelly.resizemode("auto")
shelly.turtlesize(5,5,3) 
shelly.forward(200)

shelly.left(90)

shelly.penup()

shelly.pendown()
shelly.hideturtle()
shelly.begin_fill()
shelly.fillcolor("blue")
shelly.circle(250) 
shelly.circle(250, 180, 30) 
shelly.end_fill()

shelly.stamp()

shelly.write("我好累")

import turtle
turtle.colormode(255)
pen = turtle.Turtle()
pen.color(255, 215, 0)
pen.pensize(5)

for i in range(5):
    pen.forward(250)
    pen.right(144)