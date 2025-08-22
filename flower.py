import turtle

# Setup screen
screen = turtle.Screen()
screen.bgcolor("#E5E1F4")  # Soft light blue

# Create turtle
flower = turtle.Turtle()
flower.speed(10)
flower.pensize(3)

# Petal colors 
petal_colors = [
    "#F7C8E0", "#C1E1DC", "#FDE2F3", "#D8B4F8", "#FFF5BA",
    "#FFB6B9", "#FAE3D9", "#BBDED6", "#8AC6D1", "#FFDAC1"
]

flower.pencolor("#93466D")

# Draw a single petal shadow with dynamic color
def draw_petal_shadow(color):
    flower.fillcolor(color)
    flower.begin_fill()
    flower.circle(100, 60)
    flower.left(120)
    flower.circle(100, 60)
    flower.left(120)
    flower.end_fill()

# Draw all petals with color cycling
for i in range(20):
    color = petal_colors[i % len(petal_colors)]
    
    flower.penup()
    flower.forward(5)  
    flower.pendown()
    draw_petal_shadow(color)
    
    flower.penup()
    flower.backward(5)  
    flower.pendown()
    draw_petal_shadow(color)
    
    flower.left(100)

# Draw the center of the flower
flower.penup()
flower.goto(0, -20)
flower.setheading(0)
flower.pendown()
flower.color("#EED02A") 
flower.begin_fill()
flower.circle(20)
flower.end_fill()

# Hide turtle and wait for click
flower.hideturtle()
screen.exitonclick()
