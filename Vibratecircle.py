import turtle

# Create turtle object
t = turtle.Turtle()
t.speed(10)
t.pencolor("red")

# Screen setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Spiral Pattern with Turtle")

# Initialize variables
a = 0
b = 0

# Move turtle to starting position
t.penup()
t.goto(0, 200)
t.pendown()

# Draw spiral pattern
while True:
    t.forward(a)
    t.right(b)
    a += 3
    b += 1
    if b == 210:
         break
#keep the window open until closed by the user
turtle.done()


