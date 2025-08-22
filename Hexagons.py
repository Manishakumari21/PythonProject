import turtle
t=turtle.Turtle()
t.speed(5)
#screen setup
screen=turtle.Screen()
screen.bgcolor("black")
list=["red","blue","green","yellow","purple"]

for i in range (150):
    t.color(list[i%5])
    t.pensize(i/10+1)
    t.forward(i)
    t.left(59)
