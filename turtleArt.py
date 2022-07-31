# Viola Dube 
# Project 3 Turtle Graphics
# This project will create a scene with a sun and a row of 3 houses

import turtle

#create turtle
yertle = turtle.Turtle()

# change the drawing icon from a triangle to a turtle shape
yertle.shape('turtle')

turtle.bgcolor('blue')

#draw sun with rays
yertle.penup()
yertle.goto(200,100)
yertle.color('yellow')
yertle.pendown()
yertle.begin_fill()
yertle.circle(50)
yertle.end_fill()

yertle.goto(200, 150)

for i in range(36):
    yertle.forward(100)
    yertle.backward(100)
    yertle.right(10)

# create green rectangle for grass
yertle.penup()
yertle.goto(-400,-325)
yertle.pendown()
yertle.color('green')
yertle.begin_fill()

for n in range(2):
    yertle.forward(800)
    yertle.left(90)
    yertle.forward(25)
    yertle.left(90)

yertle.end_fill()

#draw a row of 3 houses
colors = ['red', 'orange', 'brown']


#draw squares for houses
yertle.penup()
yertle.forward(75)
yertle.pendown()
for m in range(3):
    yertle.color(colors[m])
    yertle.begin_fill()
    for j in range(4):
        yertle.forward(175)
        yertle.left(90)
    yertle.end_fill()
    yertle.penup()
    yertle.forward(225)
    yertle.pendown()

    
# draw triangles for roofs on houses
yertle.penup()
yertle.color('gray')
yertle.goto(-325, -150)
yertle.pendown

yertle.begin_fill()
yertle.left(60)
yertle.forward(175)
yertle.right(120)
yertle.forward(175)
yertle.right(120)
yertle.forward(175)
yertle.end_fill()

yertle.penup()
yertle.goto(75, -150)
yertle.pendown()
yertle.begin_fill()
yertle.right(60)
yertle.forward(175)
yertle.left(120)
yertle.forward(175)
yertle.left(120)
yertle.forward(175)
yertle.end_fill()

yertle.penup()
yertle.goto(125, -150)
yertle.pendown()
yertle.begin_fill()
yertle.left(60)
yertle.forward(175)
yertle.right(120)
yertle.forward(175)
yertle.right(120)
yertle.forward(175)
yertle.end_fill()

#draw door on houses
yertle.penup()
yertle.color('black');
yertle.goto(-300, -400);
yertle.left(180); #change diretion of turtle
yertle.pendown()

for i in range(3):
    yertle.begin_fill()
    for j in range(2):
        yertle.forward(50)
        yertle.left(90)
        yertle.forward(175)
        yertle.left(90)
    yertle.end_fill()
    yertle.penup()
    yertle.forward(225)
    yertle.pendown()
    

#draw window on houses
yertle.penup()
yertle.goto(-225, -300)
yertle.pendown()

for j in range(3):
    yertle.begin_fill()
    for w in range(4):
        yertle.forward(60)
        yertle.left(90)      
    yertle.end_fill()
    yertle.penup()
    yertle.forward(225)
    yertle.pendown()




yertle.hideturtle()

