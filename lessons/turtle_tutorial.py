from turtle import Turtle, colormode, done
colormode(255)
leo: Turtle = Turtle()

leo.color(99, 204, 250)

i: int = 0
#while (i < 4):
#    leo.forward(300)
#    leo.left(90)
#    i = i + 1

leo.penup()
leo.pendown()
leo.speed(9000)
leo.goto(0,-320)
leo.goto(0, 50)
leo.hideturtle()
i: int = 0

while (i < 120):
    leo.forward(1)
    leo.right(1)
    i = i + 1
i = 0
while (i < 75):
    leo.forward(1)
    leo.right(-1)
    i += 1
i = 0
while (i<135):
    leo.forward(1.5)
    leo.right(1)
    i += 1
i = 0
leo.forward(20)
while (i<135):
    leo.forward(1.5)
    leo.right(1)
    i += 1
i = 0
while (i < 75):
    leo.forward(1)
    leo.right(-1)
    i += 1
i = 0
while (i < 120):
    leo.forward(1)
    leo.right(1)
    i = i + 1


leo.end_fill()
# code for shape to be filled 


done()