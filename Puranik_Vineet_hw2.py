import turtle
t = turtle.Turtle()

# Draw a Square and fill  with Red
t.color('red')
t.fillcolor('red')
t.begin_fill()
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.end_fill()
# Draw a Circle and fill  with Green
t.color('green')
t.fillcolor('green')
t.penup()
t.begin_fill()
t.forward(200)
t.pendown()
t.circle(50)
t.end_fill()
# Draw a Triangle and fill with Blue
t.color('blue')
t.fillcolor('blue')
t.penup()
t.left(120)
t.forward(250)
t.pendown()
t.begin_fill()
t.right(120)
t.backward(90)
t.right(90)
t.forward(90)
t.end_fill()
#Trace the letter of your last name (P)
t.color('orange')
t.penup()
t.left(90)
t.forward(-200)
t.pendown()
t.pendown()
t.forward(100)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.penup()
t.end_fill()

# All Done
turtle.done()